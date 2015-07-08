from Gaudi.Configuration import *
from Configurables import DaVinci
from Configurables import GaudiSequencer

simulation=False

stream='Bhadron'
line='B2XEtaB2etapKstarLine'

# configure an algorithm to substitute particles
from Configurables import SubstitutePID
subs = SubstitutePID(
    'PimforKm',
    Code = "DECTREE('[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> pi- pi+ gamma)]CC')",
    # note that SubstitutePID can't handle automatic CC
    Substitutions = {
    'Bottom -> (Meson -> K+ ^pi-) Meson': 'K-',
    'Bottom -> (Meson -> K- ^pi+) Meson': 'K+',
    }
)

from PhysSelPython.Wrappers import Selection
from PhysSelPython.Wrappers import SelectionSequence
from PhysSelPython.Wrappers import DataOnDemand

# Stream and stripping line we want to use
tesLoc = '/Event/{0}/Phys/{1}/Particles'.format(stream, line)
# get the selection(s) created by the stripping
strippingSels = [DataOnDemand(Location=tesLoc)]

# create a selection using the substitution algorithm
selSub = Selection(
    'PimforKm_sel',
    Algorithm=subs,
    RequiredSelections=strippingSels
)

selSeq = SelectionSequence('selSeq', TopSelection=selSub)


from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple("PimforKmTuple")
tuple.Decay="[B0 -> ^(Meson -> ^K+ ^K-) ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"
tuple.Branches={"B0":"[B0 -> (Meson -> K+ K-) (eta_prime -> pi- pi+ gamma)]CC"}
tuple.Inputs=[selSeq.outputLocation()]

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

#===========================REFIT WITH DAUGHTERS AND PV CONSTRAINED======================
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

########################################=LOKI FUNCOR VARIABLES===============================================

tuple.addBranches({'Kstar' : '[B0 -> ^(K*(892)0 -> K+ K-) (eta_prime -> pi- pi+ gamma)]CC',
                   'eta_prime' : '[B0 -> (K*(892)0 -> K+ K-) ^(eta_prime -> pi- pi+ gamma)]CC',
                   'Kplus' : '[B0 -> (K*(892)0 -> ^K+ K-) (eta_prime -> pi- pi+ gamma)]CC',
                   'piminus' : '[B0 -> (K*(892)0 -> K+ ^K-) (eta_prime -> pi- pi+ gamma)]CC',
                   'piplus' : '[B0 -> (K*(892)0 -> K+ K-) (eta_prime -> pi- ^pi+ gamma)]CC',
                   'piminus0' : '[B0 -> (K*(892)0 -> K+ K-) (eta_prime -> ^pi- pi+ gamma)]CC',
                   'gamma' : '[B0 -> (K*(892)0 -> K+ K-) (eta_prime -> pi- pi+ ^gamma)]CC'})

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
    'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(-321 == ABSID)|(321 == ABSID),PT)',
    'SUM_PCHI2= SUMTREE((211 == ABSID)|(-211 == ABSID)|(-321 == ABSID)|(321 == ABSID),TRPCHI2)'
    ]
B0_hybrid.Preambulo=preamble

B0_hybrid.Variables = {
    'max_pt_track' : 'TRACK_MAX_PT',
    'min_pt_track' : 'TRACK_MIN_PT',
    'sum_track_pt' : 'SUMTRACK_PT',
    'sum_pchi2' : 'SUM_PCHI2',
    'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))',
    'eta':'ETA'
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


#==============================TRIGGER DECISIONS==============================


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
DaVinci().RootInTES='/Event/{0}'.format(stream)
DaVinci().UserAlgorithms+=[tuple]
DaVinci().TupleFile="Output.root"
DaVinci().HistogramFile="histos.root"
DaVinci().DataType='2012'
DaVinci().EvtMax=-1
DaVinci().Lumi=True
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=False


from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
       './00041836_00000057_1.bhadron.mdst'
        ], clear=True)





