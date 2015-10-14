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
    MyLines= ["StrippingB2XEtaB2eta3piKstarLine"]

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

line = 'B2XEtaB2eta3piKstarLine'

tuple=DecayTreeTuple()
tuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta -> ^pi- ^pi+ ^(pi0 -> ^gamma ^gamma))]CC"
tuple.Branches={"B0":"[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))]CC"}
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
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/ConsAll')
tuple.B0.ConsAll.Verbose=True
tuple.B0.ConsAll.constrainToOriginVertex=True
tuple.B0.ConsAll.daughtersToConstrain = ["K*(892)0","eta"]
#==============================REFIT WITH ETA, PI0 AND PV CONTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFit')
tuple.B0.PVFit.Verbose=True
tuple.B0.PVFit.constrainToOriginVertex=True
tuple.B0.PVFit.daughtersToConstrain = ["eta","pi0"]
#==============================REFIT WITH ONLY ETA AND PV CONSTRAINED==========================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitEtaOnly')
tuple.B0.PVFitEtaOnly.Verbose=True
tuple.B0.PVFitEtaOnly.constrainToOriginVertex=True
tuple.B0.PVFitEtaOnly.daughtersToConstrain = ["eta"]
#==============================REFIT WITH ONLY K* CONSTRAINED===================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/KStarOnly')
tuple.B0.KStarOnly.Verbose=True
tuple.B0.KStarOnly.constrainToOriginVertex=True
tuple.B0.KStarOnly.daughtersToConstrain = ["K*(892)0"]
#==============================REFIT WITH ONLY  PV CONTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVOnly')
tuple.B0.PVOnly.Verbose=True
tuple.B0.PVOnly.constrainToOriginVertex=True
#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Conskstar_eta')
tuple.B0.Conskstar_eta.Verbose=True
tuple.B0.Conskstar_eta.constrainToOriginVertex=False
tuple.B0.Conskstar_eta.daughtersToConstrain = ["K*(892)0","eta"]

#========================================REFIT WITH NOTHING CONSTRAINED========================================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/Consnothing')
tuple.B0.Consnothing.Verbose=True
tuple.B0.Consnothing.constrainToOriginVertex=False

#========================================LOKI FUBNCTOR VARIABLES========================================

tuple.addBranches({'Kstar' : '[B0 -> ^(K*(892)0 -> K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'eta' : '[B0 -> (K*(892)0 -> K+ pi-) ^(eta -> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'Kplus' : '[B0 -> (K*(892)0 -> ^K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'piminus' : '[B0 -> (K*(892)0 -> K+ ^pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'piplus' : '[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- ^pi+ (pi0 -> gamma gamma))]CC',
                   'piminus0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta -> ^pi- pi+ (pi0 -> gamma gamma))]CC',
                   'gamma' : '[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- pi+ (pi0 -> ^gamma gamma))]CC',
                   'gamma0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- pi+ (pi0 -> gamma ^gamma))]CC',
                   'pi0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta -> pi- pi+ ^(pi0 -> gamma gamma))]CC'})


from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,ETA,TRPCHI2
B0_hybrid=tuple.B0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_B0')
Kstar_hybrid=tuple.Kstar.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kstar')
eta_hybrid=tuple.eta.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_eta')
Kplus_hybrid=tuple.Kplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kplus')
piminus_hybrid=tuple.piminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus')
piplus_hybrid=tuple.piplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piplus')
piminus0_hybrid=tuple.piminus0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus0')
gamma_hybrid=tuple.gamma.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma')
gamma0_hybrid=tuple.gamma0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma0')
pi0_hybrid=tuple.pi0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_pi0')

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

eta_hybrid.Variables ={
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
gamma0_hybrid.Variables = {
    'eta':'ETA'
    }
pi0_hybrid.Variables = {
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


from Configurables import TupleToolL0Calo

tuple.Kplus.addTool(TupleToolL0Calo,name="KplusL0Calo")
tuple.Kplus.ToolList += ["TupleToolL0Calo/KplusL0Calo"]
tuple.Kplus.KplusL0Calo.WhichCalo="HCAL"

tuple.piplus.addTool(TupleToolL0Calo,name="piplusL0Calo")
tuple.piplus.ToolList += ["TupleToolL0Calo/piplusL0Calo"]
tuple.piplus.piplusL0Calo.WhichCalo="HCAL"

tuple.piminus.addTool(TupleToolL0Calo,name="piminusL0Calo")
tuple.piminus.ToolList += ["TupleToolL0Calo/piminusL0Calo"]
tuple.piminus.piminusL0Calo.WhichCalo="HCAL"

tuple.piminus0.addTool(TupleToolL0Calo,name="piminus0L0Calo")
tuple.piminus0.ToolList += ["TupleToolL0Calo/piminus0L0Calo"]
tuple.piminus0.piminus0L0Calo.WhichCalo="HCAL"



etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"]


from Configurables import MCDecayTreeTuple
mctuple=MCDecayTreeTuple("mctuple")
mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

mctuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta -> ^pi- ^pi+ ^(pi0-> ^gamma ^gamma))]CC"

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



#from GaudiConf import IOHelper

# Use the local input data
#IOHelper().inputFiles([
 #   '00038851_00000006_2.AllStreams.dst'
#], clear=True)

