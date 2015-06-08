from Gaudi.Configuration import *
from Configurables import GaudiSequencer
from Configurables import DaVinci

simulation=False

from Configurables import EventNodeKiller
eventNodeKiller = EventNodeKiller('DAQkiller')
eventNodeKiller.Nodes = ['DAQ','pRec']
#MySequencer.Members+=[eventNodeKiller]

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta -> ^pi- ^pi+ ^(pi0 -> ^gamma ^gamma))]CC"
tuple.Branches={"B0":"[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma)]CC"}
tuple.Inputs=["/Event/Bhadron/Phys/B2XEtaB2eta3piKstarLine/Particles"]

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
    #, "TupleToolMCTruth"
    #, "TupleToolMCBackgroundInfo"
    , "TupleToolCaloHypo"
    #, "TupleToolTrackIsolation"
    ]

tuple.addTool(TupleToolDecay,name="B0")
from Configurables import TupleToolDecayTreeFitter

tuple.B0.addTool(TupleToolDecayTreeFitter("PVFit"))
tuple.B0.PVFit.Verbose=True
tuple.B0.PVFit.constrainToOriginVertex=True
tuple.B0.PVFit.daughtersToConstrain = ["K*(892)0","eta"]
tuple.B0.ToolList+=["TupleToolDecayTreeFitter/PVFit"]

from Configurables import TupleToolTISTOS
tistos = tuple.B0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
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



DaVinci().InputType='MDST'
#DaVinci().RootInTES='/Event/Bhadron/'
DaVinci().UserAlgorithms+=[eventNodeKiller,tuple]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2011'
DaVinci().EvtMax=-1
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=False


                   




