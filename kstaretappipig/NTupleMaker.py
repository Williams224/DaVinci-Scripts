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
    , "TupleToolCaloHypo"
    , "TupleToolTrackIsolation"
    ]


tuple.addTool(TupleToolDecay,name="B0")

from Configurables import TupleToolDecayTreeFitter

#========================================REFIT WITH DAUGHTERS AND PV CONSTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFit')
tuple.B0.PVFit.Verbose=True
tuple.B0.PVFit.constrainToOriginVertex=True
tuple.B0.PVFit.daughtersToConstrain = ["K*(892)0","eta_prime"]

#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Conskstar_etap')
tuple.B0.Conskstar_etap.Verbose=True
tuple.B0.Conskstar_etap.constrainToOriginVertex=False
tuple.B0.Conskstar_etap.daughtersToConstrain = ["K*(892)0","eta_prime"]

#========================================REFIT WITH NOTHING CONSTRAINED========================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Consnothing')
tuple.B0.Consnothing.Verbose=True
tuple.B0.Consnothing.constrainToOriginVertex=False

#========================================LOKI FUBNCTOR VARIABLES========================================

tuple.addBranches({'Kstar' : '[B0 -> ^(K*(892)0 -> K+ pi-) (eta_prime -> pi- pi+ gamma)]CC',
                   'eta_prime' : '[B0 -> (K*(892)0 -> K+ pi-) ^(eta_prime -> pi- pi+ gamma)]CC',
                   'Kplus' : '[B0 -> (K*(892)0 -> ^K+ pi-) (eta_prime -> pi- pi+ gamma)]CC',
                   'piminus' : '[B0 -> (K*(892)0 -> K+ ^pi-) (eta_prime -> pi- pi+ gamma)]CC',
                   'piplus' : '[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> pi- ^pi+ gamma)]CC',
                   'piminus0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> ^pi- pi+ gamma)]CC',
                   'gamma' : '[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> pi- pi+ ^gamma)]CC'})


from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,ETA,TRPCHI2
B0_hybrid=tuple.B0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_B0')
Kstar_hybrid=tuple.Kstar.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kstar')
eta_prime_hybrid=tuple.eta_prime.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_eta_prime')
Kplus_hybrid=tuple.Kplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kplus')
piminus_hybrid=tuple.piminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus')
piplus_hybrid=tuple.piplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piplus')
piminus0_hybrid=tuple.piminus0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus0')
gamma_hybrid=tuple.gamma.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma')

preamble=[
    'TRACK_MAX_PT= MAXTREE(PT, ISBASIC & HASTRACK, -666)',
    'TRACK_MIN_PT= MINTREE(PT, ISBASIC & HASTRACK)',
    'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID),PT)',
    'SUM_PCHI2= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID),TRPCHI2)'
    ]
B0_hybrid.Preambulo=preamble

B0_hybrid.Variables = {
    'max_pt_track' : 'TRACK_MAX_PT',
    'min_pt_track' : 'TRACK_MIN_PT',
    'sum_track_pt' : 'SUMTRACK_PT',
    'sum_pchi2' : 'SUM_PCHI2',
    'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))',
    'eta' :'ETA'
    }

Kstar_hybrid.Variables ={
    'branch_mass':'MM',
    'eta': 'ETA'
 }

eta_prime_hybrid.Variables ={
    'branch_mass':'MM',
    'eta': 'ETA'
    }

Kplus_hybrid.Variables ={
    'eta': 'ETA'
    }

piminus_hybrid.Variables ={
    'eta': 'ETA'
    }

piplus_hybrid.Variables ={
    'eta': 'ETA'
    }

piminus0_hybrid.Variables ={
    'eta': 'ETA'
    }

gamma_hybrid.Variables = {
    'eta':'ETA'
    }

#==============================TRIGGER DECISIONS==============================-

                 

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

mctuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta_prime -> ^rho(770)0 ^gamma)]CC"

MySequencer.Members.append(etuple)
MySequencer.Members.append(tuple)
MySequencer.Members.append(mctuple)

DaVinci().InputType='DST'
DaVinci().UserAlgorithms+=[MySequencer]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=1000
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=simulation



from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
    './00038839_00000002_2.AllStreams.dst'
], clear=True)

