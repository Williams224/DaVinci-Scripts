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
        
        from Configurables import PhysConf
        PhysConf().CaloReProcessing=True
        
        stripping="stripping21"
        config=strippingConfiguration(stripping)
        archive=strippingArchive(stripping)
        streams=buildStreams(stripping=config,archive=archive)
        
        MyStream= StrippingStream("MyStream")
        MyLines= ["StrippingB2CharmlessQ2B3piSelectionLine"]
        
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

        from Configurables import StrippingReport
        sr= StrippingReport(Selections =sc.selections())

        StripSequencer = GaudiSequencer('StripSequencer')
        StripSequencer.Members= [sc.sequence(),sr]
        StripSequencer.IgnoreFilterPassed =True
        DaVinci().appendToMainSequence([event_node_killer,StripSequencer])
                                                                                                            

############################################################################################

from PhysSelPython.Wrappers import Selection
from PhysSelPython.Wrappers import SelectionSequence
from PhysSelPython.Wrappers import DataOnDemand, AutomaticData

from Configurables import CombineParticles, FilterDesktop
from StandardParticles import StdLoosePions

#from PhysConf.Filters import LoKi_Filters
#fltrs = LoKi_Filters(
 # STRIP_Code = "HLT_PASS('StrippingBetaSQ2B3piSelectionLineDecision')")

stream='AllStreams'
line='B2CharmlessQ2B3piSelectionLine'
tesLoc='/Event/Phys/{0}/Particles'.format(line)

from Configurables import FilterInTrees

rho_list = FilterInTrees( 'rho_list',Code= "'rho(770)0'==ABSID")

rho_Sel = Selection("rho_Sel",
                    Algorithm=rho_list,
                    RequiredSelections = [AutomaticData(Location=tesLoc)]
                    )

rho_Seq = SelectionSequence("rho_Seq",TopSelection = rho_Sel)

pion_list = FilterInTrees('pion_list',Code= "('pi+'==ABSID) & (PT>500.0*MeV) & (TRGHOSTPROB<0.5)")

pion_Sel = Selection("pion_Sel",
                     Algorithm = pion_list,
                     RequiredSelections = [AutomaticData(Location = tesLoc)]
                     )

pion_Seq = SelectionSequence("pion_Seq",TopSelection = pion_Sel)


from StandardParticles import StdLooseAllPhotons

PhotonFilter = FilterDesktop("PhotonFilter",Code = "(PT >1.0*MeV)")

PhotonSel = Selection("PhotonSel",
                      Algorithm=PhotonFilter,
                      RequiredSelections=[StdLooseAllPhotons]
                      )



make_etap = CombineParticles ("make_etap",
                              DecayDescriptor= "eta_prime -> rho(770)0 gamma",
                              CombinationCut = "(ADAMASS('eta_prime')<100.0*MeV)&(ACUTDOCACHI2(10.0,''))",
                              MotherCut = "(PT>2000.0*MeV)&(VFASPF(VCHI2/VDOF)<10.0)"
                              )

etap_selection = Selection("etap_selection",
                           Algorithm= make_etap,
                           RequiredSelections=[PhotonSel,rho_Sel]
                           )

preambulo=[
"rho_px= CHILD (PX,1,1 ) " ,
"rho_py=CHILD  (PY,1,1 )" ,
"rho_pz=CHILD (PZ,1,1 ) ",
"rho_E= CHILD (E,1,1 ) " ,
"pi_px= CHILD (PX,2 ) " ,
"pi_py= CHILD (PY,2 ) " ,
"pi_pz= CHILD (PZ,2 ) " ,
"pi_E= CHILD (E,2) " ,
"pi_PT=CHILD (PT,2) " ,
"rhopi_px=  rho_px + pi_px",
"rhopi_py=  rho_py + pi_py",
"rhopi_pz=  rho_pz + pi_pz",
"rhopi_E=   rho_E  + pi_E",
"IM_rhopi = sqrt(rhopi_E**2 - rhopi_px**2 - rhopi_py**2 - rhopi_pz**2)"
]


makeBu= CombineParticles("makeBu",
                        Preambulo=preambulo,
                       DecayDescriptors = ['[B+ -> eta_prime pi+]cc'],
                         CombinationCut="(AM>3000.0) & (AM<10000.0) & (ACUTDOCACHI2(15.0,''))",
                     MotherCut ="(VFASPF(VCHI2/VDOF)<20.0)" 
                    )

Bu_sel = Selection("Bu_sel",
                 Algorithm= makeBu,
                 RequiredSelections=[etap_selection,pion_Sel]
                )


#KaonList= AutomaticData(Location= 'Phys/StdAllNoPIDsKaons/Particles')
#from CommonParticles import StdNoPIDsKaons
#FilteredKaons=FilterDesktop("FilteredKaons",Code="(PT >1200.0*MeV)")

#KaonSel= Selection("KaonSel",Algorithm=FilteredKaons, RequiredSelections=[StdNoPIDsKaons])

#makeBu= CombineParticles("makeBu",
#			 DecayDescriptors = ['[B+ -> eta_prime K+]cc'],
#			 CombinationCut="(AM> 3000.0) & (AM<10000.0)",
#			 MotherCut= "(VFASPF(VCHI2/VDOF)<20.0)"
#			 )

#Bu_sel = Selection("Bu_sel",
#		   Algorithm = makeBu,
#		   RequiredSelections=[etap_selection,pion_Sel,FilteredKaons]
#		   )

Bu_selSeq = SelectionSequence("Bu_selSeq",TopSelection=Bu_sel)

from Configurables import PrintDecayTree

pt= PrintDecayTree(Inputs=[Bu_selSeq.outputLocation()])

from Configurables import SubstitutePID
SubKToPi = SubstitutePID (name = "SubKToPi",
                         Code = "DECTREE('[(B+ -> eta_prime pi+),(B- -> eta_prime pi-)]')",
                          Substitutions = {
                                'B+ -> eta_prime ^pi+' : 'K+',
                                  'B- -> eta_prime ^pi-' : 'K-',
                          }
                         )
BuK_Sel=Selection("BuK_Sel",Algorithm=SubKToPi,RequiredSelections=[Bu_sel])

BuKFilter= FilterDesktop("BuKFilter",Code="(BPVDIRA>0.9995)&(BPVIPCHI2()<20.0) & (VFASPF(VCHI2/VDOF)<15.0) & (PT>1000.0*MeV) & (M>4529.0*MeV) & (M<6029.0*MeV)")

BuKFilteredSel = Selection("BuKFilteredSel",Algorithm=BuKFilter,RequiredSelections=[BuK_Sel])

BuKFilteredSel_Seq= SelectionSequence("BuKFilteredSel_Seq",TopSelection=BuKFilteredSel)




#from SelPy.graph import graph
#graph(BuSel, format='png')

from Configurables import DecayTreeTuple
from Configurables import TupleToolL0Calo
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[B+ -> ^K+ ^(eta_prime -> ^(rho(770)0 -> ^pi+ ^pi-) ^gamma)]CC"
tuple.addBranches({'Bu':"[B+ -> K+ (eta_prime -> (rho(770)0 -> pi+ pi-) gamma)]CC"})
tuple.Inputs=[BuKFilteredSel_Seq.outputLocation()]
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
tuple.Bu.DTF.Verbose=False
tuple.Bu.DTF.constrainToOriginVertex=True
tuple.Bu.DTF.UpdateDaughters = True

#===========================REFIT WITH JUST PV CONSTRAINED======================
tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTFEtapFixed')
tuple.Bu.DTFEtapFixed.daughtersToConstrain = ["eta_prime"]
tuple.Bu.DTFEtapFixed.Verbose=True
tuple.Bu.DTFEtapFixed.constrainToOriginVertex=False
tuple.Bu.DTFEtapFixed.UpdateDaughters = True

#==============================REFIT WITH K SWAPPED FOR PI ALL CONSTRAINED ==============================
tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTFKforpi')
tuple.Bu.DTFKforpi.Verbose=True
tuple.Bu.DTFKforpi.constrainToOriginVertex=False
tuple.Bu.DTFKforpi.daughtersToConstrain = ["eta_prime"]
tuple.Bu.DTFKforpi.Substitutions={
	"B+ -> ^K+ (eta_prime -> (rho(770)0 -> pi- pi+) gamma)" : "pi+",
	"B- -> ^K- (eta_prime -> (rho(770)0 -> pi- pi+) gamma)" : "pi-",
	    }

########################################=LOKI FUNCTOR VARIABLES===============================================

tuple.addBranches({ 'Kaon' : '[[B+]cc -> ^K+ (eta_prime -> (rho(770)0 -> pi+ pi-) gamma)]CC',
		    'eta_prime' : '[[B+]cc -> K+ ^(eta_prime -> (rho(770)0 -> pi+ pi-) gamma)]CC',
		    'piminus' : '[[B+]cc -> K+ (eta_prime -> (rho(770)0 -> pi+ ^pi-) gamma)]CC',
		    'piplus' : '[[B+]cc -> K+ (eta_prime -> (rho(770)0 -> ^pi+ pi-) gamma)]CC',
		    'gamma' : '[[B+]cc -> K+ (eta_prime -> (rho(770)0 ->pi+ pi-) ^gamma)]CC',
		    'rho' : '[[B+]cc -> K+ (eta_prime -> ^(rho(770)0 ->pi+ pi-) gamma)]CC',
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
rho_hybrid=tuple.rho.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_rho')

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
rho_hybrid.Variables = {
	'Mass' : 'MM',
	'ETA' : 'ETA'
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

mctuple.Decay="[[B+]cc -> ^K+ ^(eta_prime -> ^(rho(770)0 -> ^pi+ ^pi-) ^gamma)]CC"



Gseq=GaudiSequencer('MyTupleSeq')
Gseq.Members += [BuKFilteredSel_Seq.sequence()]
Gseq.Members.append(etuple)
Gseq.Members += [tuple]
Gseq.Members.append(mctuple)
#DaVinci().EventPreFilters = fltrs.filters ('Filters')
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





