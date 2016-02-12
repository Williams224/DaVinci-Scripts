from Gaudi.Configuration import *
from GaudiKernel.SystemOfUnits import *
from Configurables import DaVinci
from Configurables import GaudiSequencer

simulation=True

if simulation:
        from Configurables import EventNodeKiller
        from StrippingConf.Configuration import StrippingConf, StrippingStream
        from StrippingSettings.Utils import strippingConfiguration
        from StrippingArchive.Utils import buildStreams
        from StrippingArchive import strippingArchive
        
        event_node_killer=EventNodeKiller('StripKiller')
        event_node_killer.Nodes=['Event/AllStreams','/Event/Strip']
        
#        from Configurables import PhysConf
 #       PhysConf().CaloReProcessing=True
        
        stripping="stripping20r0p2"
        config=strippingConfiguration(stripping)
        archive=strippingArchive(stripping)
        streams=buildStreams(stripping=config,archive=archive)
        
        MyStream= StrippingStream("MyStream")
        MyLines= ["StrippingBetaSQ2B3piSelectionLine"]
        
        for stream in streams:
            for line in stream.lines:
                if line.name() in MyLines:
                    MyStream.appendLines( [ line ])
                    
	from Configurables import ProcStatusCheck
        filterBadEvents=ProcStatusCheck()
        
        sc=StrippingConf( Streams= [ MyStream ],
                          MaxCandidates = 2000,
                          AcceptBadEvents = False,
                          BadEventSelection = filterBadEvents,
			  HDRLocation       =  "SomeNoExistingLocation" )
        
        DaVinci().appendToMainSequence([event_node_killer,sc.sequence()])
                                                                                                            

############################################################################################




from PhysSelPython.Wrappers import Selection
from PhysSelPython.Wrappers import SelectionSequence
from PhysSelPython.Wrappers import DataOnDemand

from Configurables import CombineParticles, FilterDesktop
from StandardParticles import StdLoosePions

stream='AllStreams'
line='BetaSQ2B3piSelectionLine'
tesLoc='/Event/{0}/Phys/{1}/Particles'.format(stream,line)

TrackList=DataOnDemand('Phys/TrackListBetaSQ2B/Particles')

PionFilter=FilterDesktop('PionFilter',
                         Code= 'PT>250.0*MeV',
                         )

PionSelection = Selection(name= 'PionSelection',
                          Algorithm = PionFilter,
                          RequiredSelections= [TrackList])

stdloosephotons = DataOnDemand('Phys/StdLooseAllPhotons/Particles')

photonfilter = FilterDesktop('photonfilter',
			     Code = 'PT> 500.0*MeV',
			     )

photonselection= Selection(name= 'gammaselection',
			   Algorithm = photonfilter,
			   RequiredSelections= [stdloosephotons])

makeeta_prime= CombineParticles('makeeta_prime',
				DecayDescriptor="eta_prime -> pi+ pi- gamma",
				CombinationCut = "(AM > 880.0*MeV) & (AM<1040.0*MeV) & (AP > 4000.0) & (APT > 1500.0)",
                                DaughtersCuts={'pi+':'ALL','pi-':'ALL','gamma':'ALL'},
				MotherCut= "(VFASPF(VCHI2/VDOF)<9.0)")

eta_primesel= Selection(name="eta_primesel",
			Algorithm = makeeta_prime,
			RequiredSelections= [PionSelection, photonselection])

stdKaons = DataOnDemand("Phys/StdLooseKaons/Particles")

#FilteredKaons = FilterDesktop('FilteredKaons',
#			      Code = 'PT>1200')

#FilteredKaonsSel = Selection(name="FilteredKaonsSel",
#			     Algorithm= FilteredKaons,
#x			     RequiredSelections =[stdKaons])

makeBu= CombineParticles('makeBu',
			 DecayDescriptor="[B+ -> eta_prime K+]cc",
			 CombinationCut ="(AM > 4900) & (AM < 5600) & (APT > 1500) & (AMAXDOCA('') < 0.04*mm)",
			 MotherCut = "(VFASPF(VCHI2/VDOF)<6.0)",
			 )

BuSel = Selection('BuSel',
		  Algorithm=makeBu,
		  RequiredSelections = [eta_primesel,stdKaons])

Buseq = SelectionSequence('Buseq',
			  TopSelection= BuSel)
		
#from SelPy.graph import graph
#graph(BuSel, format='png')

from Configurables import DecayTreeTuple
from Configurables import TupleToolL0Calo
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[[B+]cc -> ^K+ ^(eta_prime -> ^pi+ ^pi- ^gamma)]CC"
tuple.addBranches({'Bu':"[[B+]cc -> K+ (eta_prime -> pi+ pi- gamma)]CC"})
tuple.Inputs=[Buseq.outputLocation()]
tuple.addTool(TupleToolL0Calo())
tuple.TupleToolL0Calo.TriggerClusterLocation="/Event/Trig/L0/Calo"
tuple.TupleToolL0Calo.WhichCalo="HCAL"


tuple.ToolList += [
    "TupleToolGeometry"
    , "TupleToolDira"
    , "TupleToolAngles"
    , "TupleToolPid"
    , "TupleToolKinematic"
    , "TupleToolPropertime"
    , "TupleToolPrimaries"
    , "TupleToolEventInfo"
    , "TupleToolTrackInfo"
    , "TupleToolVtxIsoln"
    , "TupleToolPhotonInfo"
    , "TupleToolMCTruth"
    , "TupleToolMCBackgroundInfo"
    , "TupleToolCaloHypo"
    , "TupleToolRecoStats"
    , "TupleToolTrackIsolation"
    ]

from Configurables import TupleToolDecay
tuple.addTool(TupleToolDecay,name="B+")
tuple.addTool(TupleToolDecay,name="eta_prime")




from Configurables import TupleToolDecayTreeFitter

#===========================REFIT WITH JUST PV CONSTRAINED======================
tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTF')
tuple.Bu.DTF.Verbose=True
tuple.Bu.DTF.constrainToOriginVertex=True

#===========================REFIT WITH JUST PV CONSTRAINED======================
tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTFEtapFixed')
tuple.Bu.DTFEtapFixed.daughtersToConstrain = ["eta_prime"]
tuple.Bu.DTFEtapFixed.Verbose=True
tuple.Bu.DTFEtapFixed.constrainToOriginVertex=True

#==============================REFIT WITH K SWAPPED FOR PI ALL CONSTRAINED ==============================
#tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTFKforpi')
#tuple.Bu.DTFKforpi.Verbose=True
#tuple.Bu.DTFKforpi.constrainToOriginVertex=True
#tuple.Bu.DTFKforpi.daughtersToConstrain = ["eta_prime"]
#tuple.Bu.DTFKforpi.Substitutions={
#	"B+ -> ^K+ (eta_prime -> (rho(770)0 -> pi- pi+) gamma)" : "pi+",
#	"B- -> ^K- (eta_prime -> (rho(770)0 -> pi- pi+) gamma)" : "pi-",
#	    }

########################################=LOKI FUNCTOR VARIABLES===============================================

tuple.addBranches({ 'Kaon' : '[[B+]cc -> ^K+ (eta_prime -> pi+ pi- gamma)]CC',
		    'eta_prime' : '[[B+]cc -> K+ ^(eta_prime -> pi+ pi- gamma)]CC',
		    'piminus' : '[[B+]cc -> K+ (eta_prime -> pi+ ^pi- gamma)]CC',
		    'piplus' : '[[B+]cc -> K+ (eta_prime -> ^pi+ pi- gamma)]CC',
		    'gamma' : '[[B+]cc -> K+ (eta_prime -> pi+ pi- ^gamma)]CC',
            })

from Configurables import TupleToolMCBackgroundInfo
tuple.Bu.addTool( TupleToolMCBackgroundInfo )
tuple.Bu.ToolList += [ "TupleToolMCBackgroundInfo" ]

from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,ETA,TRPCHI2

#eventtupletool=tuple.addTupleTool('LoKi::Hybrid::EventTupleTool/ETT')
#eventtupletool.VOID_Variables = {
#    "nTracks" : "TrSOURCE('Rec/Track/Best') >> TrSIZE"
 #   ,"nPVs"   : "CONTAINS('Rec/Vertex/Primary')"
   #   }

Bu_hybrid=tuple.Bu.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Bu')
Kaon_hybrid=tuple.Kaon.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kaon')
eta_prime_hybrid=tuple.eta_prime.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_eta_prime')
piminus_hybrid=tuple.piminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus')
piplus_hybrid=tuple.piplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piplus')
gamma_hybrid=tuple.gamma.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma')


preamble=[
	'TRACK_MAX_PT= MAXTREE(PT, ISBASIC & HASTRACK, -666)',
	'TRACK_MIN_PT= MINTREE(PT, ISBASIC & HASTRACK)',
	'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),PT)',
	'SUM_PCHI2= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),TRPCHI2)',
	]
Bu_hybrid.Preambulo=preamble

Bu_hybrid.Variables = {
	'max_pt_track' : 'TRACK_MAX_PT',
	'min_pt_track' : 'TRACK_MIN_PT',
	'sum_track_pt' : 'SUMTRACK_PT',
	'sum_pchi2' : 'SUM_PCHI2',
	'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))',
	'ETA':'ETA'
	}

Kaon_hybrid.Variables ={
	'Mass':'MM',
	'ETA': 'ETA'
	}

eta_prime_hybrid.Variables ={
	'ETA': 'ETA'
	}

piminus_hybrid.Variables ={
	'ETA': 'ETA'
	}

piplus_hybrid.Variables ={
	'ETA': 'ETA'
	}

gamma_hybrid.Variables = {
	'ETA':'ETA'
	}

#==============================MassSubs=====================================
from Configurables import TupleToolSubMass

tuple.Bu.addTool(TupleToolSubMass)
tuple.Bu.ToolList += ["TupleToolSubMass"]
tuple.Bu.TupleToolSubMass.Substitution += ["K+ => pi+"]
tuple.Bu.TupleToolSubMass.Substitution += ["K+ => p+"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi+ => p+"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi+ => K+"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi- => p~-"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi- => K-"]
tuple.Bu.TupleToolSubMass.Substitution += ["gamma => e-"]
tuple.Bu.TupleToolSubMass.Substitution += ["gamma => e+"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi+ => mu+"]
tuple.Bu.TupleToolSubMass.Substitution += ["pi- => mu-"]
tuple.Bu.TupleToolSubMass.DoubleSubstitution += ["K+/pi- => pi+/K-"]
tuple.Bu.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => pi-/pi+"]
tuple.Bu.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => mu+/mu-"]


#==============================TRIGGER DECISIONS==============================


from Configurables import TupleToolTISTOS
tistos = tuple.Bu.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
tistos.VerboseL0=True
tistos.VerboseHlt1=True
tistos.VerboseHlt2=True
tistos.TriggerList=["L0PhotonDecision",
                    "L0ElectronDecision",
                    "Hlt1TrackPhotonDecision",
                    "Hlt1TrackAllL0Decision",
                    "Hlt1TrackMuonDecision",
                    "Hlt1TrackForwardPassThroughDecision",
                    "Hlt1TrackForwardPassThroughLooseDecision",
                    "Hlt1SingleElectronNoIPDecision",
                    "L0HadronDecision",
                    "L0LocalPi0Decision",
                    "L0GlobalPi0Decision",
                    "L0MuonDecision",
                    "Hlt2Topo2BodyBBDTDecision",
                    "Hlt2Topo3BodyBBDTDecision",
                    "Hlt2Topo4BodyBBDTDecision",
                    "Hlt2RadiativeTopoTrackTOSDecision",
                    "Hlt2RadiativeTopoPhotonL0Decision",
                    "Hlt2TopoRad2BodyBBDTDecision",
                    "Hlt2TopoRad2plus1BodyBBDTDecision",
                    "Hlt2Topo2BodySimpleDecision",
                    "Hlt2Topo3BodySimpleDecision",
                    "Hlt2Topo4BodySimpleDecision"]

from Configurables import TupleToolMCTruth
tuple.addTool(TupleToolMCTruth)
tuple.ToolList += ["TupleToolMCTruth"]
tuple.TupleToolMCTruth.ToolList += [
	"MCTupleToolHierarchy",
	"MCTupleToolKinematic",
	#    "MCTupleToolDecayType",
	#   "MCTupleToolReconstructed",
	#  "MCTupleToolPID",
	# "MCTupleToolP2VV",
	#    "MCTupleToolAngles",
	#    "MCTupleToolInteractions",
	#   "MCTupleToolPrimaries",
	#  "MCTupleToolPrompt"
	]

from Configurables import TupleToolL0Calo

tuple.Kaon.addTool(TupleToolL0Calo,name="KaonL0Calo")
tuple.Kaon.ToolList += ["TupleToolL0Calo/KaonL0Calo"]
tuple.Kaon.KaonL0Calo.WhichCalo="HCAL"

tuple.piplus.addTool(TupleToolL0Calo,name="piplusL0Calo")
tuple.piplus.ToolList += ["TupleToolL0Calo/piplusL0Calo"]
tuple.piplus.piplusL0Calo.WhichCalo="HCAL"

tuple.piminus.addTool(TupleToolL0Calo,name="piminusL0Calo")
tuple.piminus.ToolList += ["TupleToolL0Calo/piminusL0Calo"]
tuple.piminus.piminusL0Calo.WhichCalo="HCAL"

etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"]

from Configurables import MCDecayTreeTuple
mctuple=MCDecayTreeTuple("mctuple")
mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

mctuple.Decay="[[B+]cc -> ^K+ ^(eta_prime -> ^pi+ ^pi- ^gamma)]CC"



Gseq=GaudiSequencer('MyTupleSeq')
Gseq.Members += [Buseq.sequence()]
Gseq.Members.append(etuple)
Gseq.Members += [tuple]
Gseq.Members.append(mctuple)

DaVinci().InputType='DST'
#DaVinci().appendToMainSequence([Gseq])
DaVinci().UserAlgorithms+=[Gseq]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=3000
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=True
DaVinci.DDDBtag='dddb-20130929-1'
DaVinci.CondDBtag='sim-20130522-1-vc-md100'

from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
    './MC_12_12103211.dst'
    ], clear=True)





