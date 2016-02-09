from Gaudi.Configuration import *
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
stream='AllStreams'
line='BetaSQ2B3piSelectionLine'
tesLoc='/Event/{0}/Phys/{1}/Particles'.format(stream,line)

rhooutput=DataOnDemand(Location='Phys/DiTracksForCharmlessBBetaSQ2B/Particles')

rhofilter=FilterDesktop('rhofilter',
			Code = 'PT>700*MeV'
			)

rhoselection = Selection(name  = 'rhoselection',
			 Algorithm = rhofilter,
			 RequiredSelections=[rhooutput]
			 )


stdloosephotons = DataOnDemand('Phys/StdLooseAllPhotons/Particles')

photonfilter = FilterDesktop('photonfilter',
			     Code = 'PT> 250*MeV',
			     )

photonselection= Selection(name= 'gammaselection',
			   Algorithm = photonfilter,
			   RequiredSelections= [stdloosephotons])

makeeta_prime= CombineParticles('makeeta_prime',
				DecayDescriptor="[eta_prime -> rho(770)0 gamma]cc",
				CombinationCut = "(AM >800)",
				MotherCut= "(VFASPF(VCHI2/VDOF)<10.0)")

eta_primesel= Selection(name="eta_primesel",
			Algorithm = makeeta_prime,
			RequiredSelections= [rhoselection, photonselection])

stdKaons = DataOnDemand("Phys/StdLooseKaons/Particles")

makeBu= CombineParticles('makeBu',
			 DecayDescriptor="[B+ -> eta_prime K+]cc",
			 CombinationCut ="(AM > 4500) & (AM < 6500)",
			 MotherCut = "(VFASPF(VCHI2/VDOF)<9.0)",
			 )

BuSel = Selection('BuSel',
		  Algorithm=makeBu,
		  RequiredSelections = [eta_primesel,stdKaons])

Buseq = SelectionSequence('Buseq',
			  TopSelection= BuSel)
		
# Build an Eta_prime

#eta_prime_daughters = {
#	'pi+' : '(PT > 200*MeV)',
#	'pi-' : '(PT> 200*MeV)',
#	'gamma' : '(PT>400*MeV)'
#	}


#CombEta_prime = CombineParticles('CombEta_prime',
#				 Inputs= ['Phys/StdAllLoosePions/Particles','Phys/StdLooseAllPhotons/Particles',StrippingSels.outputLocation()],
#				 DecayDescriptor = 'eta_prime -> rho(770)0 gamma',
#				 DaughtersCuts=eta_prime_daughters,
#				 CombinationCut='(APT>1200*MeV)',
#				 MotherCut = '(VFASPF(VCHI2/VDOF)<10.0)')

#etapsel=Selection('etapsel', Algorithm=CombEta_prime,RequiredSelections=[StdAllLoosePions,StdLooseAllPhotons,StrippingSels])

#Bu_daughters = {
#	'K+' : '(PT>1000*MeV)'
#	}

#BuComb=CombineParticles('BuComb',
#			Inputs=[etapsel.outputLocation(),'Phys/StdAllLooseKaons/Particles'],
#			DecayDescriptor ='B+ -> K+ eta_prime',
#			DaughtersCuts = Bu_daughters,
#			CombinationCut= "in_range(4500,AM,5600)",
#			MotherCut = '(VFASPF(VCHI2/VDOF) <10.0)'
#			)

#BuSel=Selection('BuSel',
#	       Algorithm=BuComb,
#	       RequiredSelections=[StdAllLooseKaons,etapsel])

#BuSelSeq = SelectionSequence('BuSelSeq',TopSelection=BuSel)
			
			

#Bu_seq=SelectionSequence('Bu_seq',TopSelection=Bu_sel)

#from SelPy.graph import graph
#graph(Bu_sel, format='png')

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[B+ -> ^K+ ^(eta_prime -> ^(rho(770)0 -> ^pi+ ^pi-) ^gamma)]CC"
#tuple.Decay="[B+ -> ^(rho(770)0 -> ^pi+ ^pi-) ^pi+]CC"
#tuple.Branches={"Bu":"[B+ -> (rho(770)0 -> pi+ pi-) pi+]CC"}
#tuple.Inputs=['Phys/{0}/Particles'.format(line)]
tuple.Inputs=[Buseq.outputLocation()]

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

tuple.addTool(TupleToolDecay,name="Bu")

from Configurables import TupleToolDecayTreeFitter

#===========================REFIT WITH DAUGHTERS AND PV CONSTRAINED======================
#tuple.Bu.addTupleTool('TupleToolDecayTreeFitter/DTF')
#tuple.Bu.DTF.Verbose=True
#tuple.Bu.DTF.constrainToOriginVertex=True

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

Gseq=GaudiSequencer('MyTupleSeq')
Gseq.Members += [Buseq.sequence()]
Gseq.Members += [tuple]
DaVinci().InputType='DST'
DaVinci().appendToMainSequence([Gseq])
#DaVinci().UserAlgorithms+=[tuple]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=5000
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=True
DaVinci.DDDBtag='dddb-20130929-1'
DaVinci.CondDBtag='sim-20130522-1-vc-md100'

from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
    '00046511_00000002_2.AllStreams.dst'
    ], clear=True)





