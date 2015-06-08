from Gaudi.Configuration import *
from Configurables import DaVinci
#from Configurables import AlgTool
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')
#For 2012 MC
DaVinci.DDDBtag='dddb-20130929-1'
DaVinci.CondDBtag='sim-20130522-1-vc-mu100'

#for 2011 MC
#DaVinci.DDDBtag='dddb-20130929'
#DaVinci.CondDBtag='sim-20130522-vc-mu100'

simulation=True



#################################################################
#Rerun with stripping21 applied

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
    MyLines= ["StrippingB2XEtaB2etapKstarLine"]

    for stream in streams:
        for line in stream.lines:
            if line.name() in MyLines:
                MyStream.appendLines( [ line ])

    from Configurables import ProcStatusCheck
    filterBadEvents=ProcStatusCheck()

    sc=StrippingConf( Streams= [ MyStream ],
                      MaxCandidates = 2000,
                      AcceptBadEvents = False,
                      BadEventSelection = filterBadEvents)

    DaVinci().appendToMainSequence([event_node_killer,sc.sequence()])
    

            
##################Creating NTuples#####################################
from Configurables import DecayTreeTuple
from Configurables import TupleToolL0Calo
from DecayTreeTuple.Configuration import *

line = 'B2XEtaB2etapKstarLine'

tuple=DecayTreeTuple()
tuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"
tuple.Branches={"B0":"[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> pi- pi+ gamma)]CC"}
tuple.Inputs=['/Event/Phys/{0}/Particles'.format(line)]
tuple.addTool(TupleToolL0Calo())
tuple.TupleToolL0Calo.TriggerClusterLocation="/Event/Trig/L0/Calo"
tuple.TupleToolL0Calo.WhichCalo="HCAL"


tuple.ToolList += [
    "TupleToolGeometry"
    , "TupleToolDira"
    , "TupleToolAngles"
   # , "TupleToolL0Calo"
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
   # , "MCTupleTOolHierachy"
    , "TupleToolCaloHypo"
    , "TupleToolTrackIsolation"
    #, "TupleToolTagging" not used in microdst
    ]

#from Configurables import TupleToolMCTruth
#from TupleToolMCTruth.Configuration import *

#tuple.addTool(TupleToolMCTruth,name="TruthM")
#tuple.ToolList+= [ "TupleToolMCTruth/TruthM"]
#tuple.TruthM.ToolList = ["MCTupleToolHierachy/Hierachy"]
#tuple.TruthM.addTool(MCTupleToolHierachy,name="Hierachy")
#tuple.TupleToolMCTruth.addTool(MCTupleToolKinematic,name="MCTupleToolKinematic")
#tuple.TupleToolMCTruth.addTool(MCTupleToolHierachy,name="MCTupleToolHierachy")
#tuple.TupleToolMCTruth.addTool(MCTupleToolPID,name="MCTupleToolPID")

tuple.addTool(TupleToolDecay,name="B0")

from Configurables import TupleToolDecayTreeFitter

#========================================REFIT WITH DAUGHTERS AND PV CONSTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/ConsPV_kstar_etap')
tuple.B0.ConsPV_kstar_etap.Verbose=True
tuple.B0.ConsPV_kstar_etap.constrainToOriginVertex=True
tuple.B0.ConsPV_kstar_etap.daughtersToConstrain = ["K*(892)0","eta_prime"]

#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Conskstar_etap')
tuple.B0.Conskstar_etap.Verbose=True
tuple.B0.Conskstar_etap.constrainToOriginVertex=False
tuple.B0.Conskstar_etap.daughtersToConstrain = ["K*(892)0","eta_prime"]

#========================================REFIT WITH NOTHING CONSTRAINED========================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Consnothing')
tuple.B0.Consnothing.Verbose=True
tuple.B0.Consnothing.constrainToOriginVertex=False



                 

from Configurables import TupleToolTISTOS
tistos=tuple.B0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
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

etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"]


from Configurables import MCDecayTreeTuple
mctuple=MCDecayTreeTuple("mctuple")
mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

mctuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta_prime -> ^rho0 ^gamma)]CC"

MySequencer.Members.append(etuple)
MySequencer.Members.append(tuple)
MySequencer.Members.append(mctuple)

DaVinci().InputType='DST'
DaVinci().UserAlgorithms+=[MySequencer]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=-1
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=simulation



from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
    './00038839_00000002_2.AllStreams.dst'
], clear=True)

