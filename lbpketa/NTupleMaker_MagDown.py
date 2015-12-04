from Gaudi.Configuration import *
from Configurables import DaVinci
#from Configurables import AlgTool
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')
#For 2012 MC
DaVinci.DDDBtag='dddb-20130929-1'
DaVinci.CondDBtag='sim-20130522-1-vc-md100'

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
    MyLines= ["StrippingB2XEtaLb2pKeta3piLine"]

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

line = 'B2XEtaLb2pKeta3piLine'

tuple=DecayTreeTuple()
tuple.Decay="[Lambda_b0 -> ^p+ ^K- ^(eta -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma))]CC"
tuple.Branches={"Lambda_b0":"[Lambda_b0 -> p+ K- (eta -> pi+ pi- (pi0 -> gamma gamma))]CC"}
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


tuple.addTool(TupleToolDecay,name="Lambda_b0")

from Configurables import TupleToolDecayTreeFitter

#========================================REFIT WITH DAUGHTERS AND PV CONSTRAINED==============================
#tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/ConsAll')
#tuple.Lambda_b0.ConsAll.Verbose=True
#tuple.Lambda_b0.ConsAll.constrainToOriginVertex=True
#tuple.Lambda_b0.ConsAll.daughtersToConstrain = ["p+","K-","eta"]
#==============================REFIT WITH ETA, PI0 AND PV CONTRAINED==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/PVFitpf')
tuple.Lambda_b0.PVFitpf.Verbose=True
tuple.Lambda_b0.PVFitpf.constrainToOriginVertex=True
tuple.Lambda_b0.PVFitpf.daughtersToConstrain = ["eta","p+","K-","pi0"]
#==============================REFIT WITH ONLY ETA AND PV CONSTRAINED==========================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/PVFit')
tuple.Lambda_b0.PVFit.Verbose=True
tuple.Lambda_b0.PVFit.constrainToOriginVertex=True
tuple.Lambda_b0.PVFit.daughtersToConstrain = ["eta","p+","K-"]
#==============================REFIT WITH ONLY K* CONSTRAINED===================================
#tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/KStarOnly')
#tuple.Lambda_b0.KStarOnly.Verbose=True
#tuple.Lambda_b0.KStarOnly.constrainToOriginVertex=True
#tuple.Lambda_b0.KStarOnly.daughtersToConstrain = ["K*(892)0"]
#==============================REFIT WITH ONLY  PV CONTRAINED==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/PVOnly')
tuple.Lambda_b0.PVOnly.Verbose=True
tuple.Lambda_b0.PVOnly.constrainToOriginVertex=True
#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/NoPVFit')
tuple.Lambda_b0.NoPVFit.Verbose=True
tuple.Lambda_b0.NoPVFit.constrainToOriginVertex=False
tuple.Lambda_b0.NoPVFit.daughtersToConstrain = ["eta","p+","K-"]

#========================================REFIT WITH NOTHING CONSTRAINED========================================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/Consnothing')
tuple.Lambda_b0.Consnothing.Verbose=True
tuple.Lambda_b0.Consnothing.constrainToOriginVertex=False

#========================================LOKI FUBNCTOR VARIABLES========================================

tuple.addBranches({
    'proton' : '[Lambda_b0 -> ^p+ K- (eta -> pi+ pi- (pi0 -> gamma gamma))]CC',
    'Kminus' : '[Lambda_b0 -> p+ ^K- (eta -> pi+ pi- (pi0 -> gamma gamma))]CC',
    'eta' : '[Lambda_b0 -> p+ K- ^(eta -> pi+ pi- (pi0 -> gamma gamma))]CC',
    'piplus':'[Lambda_b0 -> p+ K- (eta -> ^pi+ pi- (pi0 -> gamma gamma))]CC',
    'piminus':'[Lambda_b0 -> p+ K- (eta -> pi+ ^pi- (pi0 -> gamma gamma))]CC',
    'pi0':'[Lambda_b0 -> p+ K- (eta -> pi+ pi- ^(pi0 -> gamma gamma))]CC',
    'gamma':'[Lambda_b0 -> p+ K- (eta -> pi+ pi- (pi0 -> ^gamma gamma))]CC',
    'gamma0':'[Lambda_b0 -> p+ K- (eta -> pi+ pi- (pi0 -> gamma ^gamma))]CC',
})


from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,ETA,TRPCHI2
Lambda_b0_hybrid=tuple.Lambda_b0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Lambda_b0')
proton_hybrid=tuple.proton.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_proton')
Kminus_hybrid=tuple.Kminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_Kminus')
eta_hybrid=tuple.eta.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_eta')
piminus_hybrid=tuple.piminus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piminus')
piplus_hybrid=tuple.piplus.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_piplus')
gamma_hybrid=tuple.gamma.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma')
gamma0_hybrid=tuple.gamma0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_gamma0')
pi0_hybrid=tuple.pi0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_pi0')

preamble=[
    'TRACK_MAX_PT= MAXTREE(PT, ISBASIC & HASTRACK, -666)',
    'TRACK_MIN_PT= MINTREE(PT, ISBASIC & HASTRACK)',
    'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),PT)',
    'SUM_PCHI2= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID)|(2212 == ABSID)|(-2212 == ABSID),TRPCHI2)'
    ]
Lambda_b0_hybrid.Preambulo=preamble

Lambda_b0_hybrid.Variables = {
    'max_pt_track' : 'TRACK_MAX_PT',
    'min_pt_track' : 'TRACK_MIN_PT',
    'sum_track_pt' : 'SUMTRACK_PT',
    'sum_pchi2' : 'SUM_PCHI2',
    'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))',
    'eta' :'ETA'
    }

proton_hybrid.Variables ={
    'eta': 'ETA'
 }

Kminus_hybrid.Variables ={
    'eta': 'ETA'
 }

eta_hybrid.Variables ={
    'branch_mass':'MM',
    'eta': 'ETA'
    }

piminus_hybrid.Variables ={
    'eta': 'ETA'
    }

piplus_hybrid.Variables ={
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

########MASS SUBSTITUTIONS#########

from Configurables import TupleToolSubMass

tuple.Lambda_b0.addTool(TupleToolSubMass)
tuple.Lambda_b0.ToolList += ["TupleToolSubMass"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["p+ => K+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["p+ => pi+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["K- => pi-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["K- => p~-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => p+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => K+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => K-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => p~-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["gamma => pi0"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["gamma => e-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["gamma => e+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi- => mu-"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi+ => mu+"]
tuple.Lambda_b0.TupleToolSubMass.Substitution += ["pi0 => eta"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["K-/p+ => p~-/K+"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => pi-/pi+"]
tuple.Lambda_b0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => mu+/mu-"]



#==============================TRIGGER DECISIONS==============================-

                 

from Configurables import TupleToolTISTOS
tistos=tuple.Lambda_b0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
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

tuple.Kminus.addTool(TupleToolL0Calo,name="KminusL0Calo")
tuple.Kminus.ToolList += ["TupleToolL0Calo/KminusL0Calo"]
tuple.Kminus.KminusL0Calo.WhichCalo="HCAL"

tuple.piplus.addTool(TupleToolL0Calo,name="piplusL0Calo")
tuple.piplus.ToolList += ["TupleToolL0Calo/piplusL0Calo"]
tuple.piplus.piplusL0Calo.WhichCalo="HCAL"

tuple.piminus.addTool(TupleToolL0Calo,name="piminusL0Calo")
tuple.piminus.ToolList += ["TupleToolL0Calo/piminusL0Calo"]
tuple.piminus.piminusL0Calo.WhichCalo="HCAL"

tuple.proton.addTool(TupleToolL0Calo,name="protonL0Calo")
tuple.proton.ToolList += ["TupleToolL0Calo/protonL0Calo"]
tuple.proton.protonL0Calo.WhichCalo="HCAL"

etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"]

from Configurables import MCDecayTreeTuple
mctuple=MCDecayTreeTuple("mctuple")
mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

mctuple.Decay="[Lambda_b0 -> ^p+ ^K- ^(eta -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma))]CC"


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
 #   '00038909_00000002_2.AllStreams.dst'
#], clear=True)

