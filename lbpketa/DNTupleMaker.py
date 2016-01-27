from Gaudi.Configuration import *
from Configurables import DaVinci
from Configurables import GaudiSequencer

simulation=False

stream='Bhadron'
line='StrippingB2XEtaLb2pKeta3piLine'

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[Lambda_b0 -> ^p+ ^K- ^(eta -> ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma))]CC"
tuple.Branches={"Lambda_b0":"[Lambda_b0 -> p+ K- (eta -> pi+ pi- (pi0 -> gamma gamma))]CC"}
tuple.Inputs=['Phys/{0}/Particles'.format(line)]

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
    , "TupleToolRecoStats"
    #, "TupleToolTrackIsolation"
    ]

tuple.addTool(TupleToolDecay,name="Lambda_b0")

from Configurables import TupleToolDecayTreeFitter

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
#==============================REFIT WITH ONLY  PV CONTRAINED==============================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/PVOnly')
tuple.Lambda_b0.PVOnly.Verbose=True
tuple.Lambda_b0.PVOnly.constrainToOriginVertex=True
#========================================REFIT WITH JUST DAUGHTERS CONSTRAINED================================
tuple.Lambda_b0.addTupleTool('TupleToolDecayTreeFitter/NoPVFit')
tuple.Lambda_b0.NoPVFit.Verbose=True
tuple.Lambda_b0.NoPVFit.constrainToOriginVertex=False
tuple.Lambda_b0.NoPVFit.daughtersToConstrain = ["eta","p+","K-"]
#==============================REFIT WITH ETA AND PV K for piCONTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitKforpi')
tuple.B0.PVFitKforpi.Verbose=True
tuple.B0.PVFitKforpi.constrainToOriginVertex=True
tuple.B0.PVFitKforpi.daughtersToConstrain = ["eta"]
tuple.B0.PVFitKforpi.Substitutions={
    "B0 -> (K*(892)0 -> ^K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))" : "pi+" ,
    "B~0 -> (K*(892)~0 -> ^K- pi+) (eta -> pi+ pi- (pi0 -> gamma gamma))" : "pi-" ,
    }

#==============================REFIT WITH ETA AND PV CONTRAINED - piminus ->K swap ==============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiminusforK')
tuple.B0.PVFitpiminusforK.Verbose=True
tuple.B0.PVFitpiminusforK.constrainToOriginVertex=True
tuple.B0.PVFitpiminusforK.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiminusforK.Substitutions={
    "B0 -> (K*(892)0 ->  K+ ^pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))" : "K-" ,
    "B~0 -> (K*(892)~0 ->  K- ^pi+) (eta -> pi+ pi- (pi0 -> gamma gamma))" : "K+" ,
    }
#==============================REFIT WITH ETA AND PV CONTRAINED - piminus0 -> Kminus swap =============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiminus0forK')
tuple.B0.PVFitpiminus0forK.Verbose=True
tuple.B0.PVFitpiminus0forK.constrainToOriginVertex=True
tuple.B0.PVFitpiminus0forK.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiminus0forK.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> ^pi- pi+ (pi0 -> gamma gamma))" : "K-" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> ^pi+ pi- (pi0 -> gamma gamma))" : "K+" ,
    }
#==============================REFIT WITH ETA AND PV CONTRAINED - piplus -> Kminus swap ============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiplusforK')
tuple.B0.PVFitpiplusforK.Verbose=True
tuple.B0.PVFitpiplusforK.constrainToOriginVertex=True
tuple.B0.PVFitpiplusforK.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiplusforK.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> pi- ^pi+ (pi0 -> gamma gamma))" : "K+" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> pi+ ^pi- (pi0 -> gamma gamma))" : "K-" ,
    }
#proton swaps
#==============================REFIT WITH ETA AND PV K for proton CONTRAINED==============================
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitKforproton')
tuple.B0.PVFitKforproton.Verbose=True
tuple.B0.PVFitKforproton.constrainToOriginVertex=True
tuple.B0.PVFitKforproton.daughtersToConstrain = ["eta"]
tuple.B0.PVFitKforproton.Substitutions={
    "B0 -> (K*(892)0 -> ^K+ pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))" : "p+" ,
    "B~0 -> (K*(892)~0 -> ^K- pi+) (eta -> pi+ pi- (pi0 -> gamma gamma))" : "p~-" ,
    }

#==============================REFIT WITH ETA AND PV CONTRAINED - piminus ->K swap ==============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiminusforproton')
tuple.B0.PVFitpiminusforproton.Verbose=True
tuple.B0.PVFitpiminusforproton.constrainToOriginVertex=True
tuple.B0.PVFitpiminusforproton.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiminusforproton.Substitutions={
    "B0 -> (K*(892)0 ->  K+ ^pi-) (eta -> pi- pi+ (pi0 -> gamma gamma))" : "p~-" ,
    "B~0 -> (K*(892)~0 ->  K- ^pi+) (eta -> pi+ pi- (pi0 -> gamma gamma))" : "p+" ,
    }
#==============================REFIT WITH ETA AND PV CONTRAINED - piminus0 -> Kminus swap =============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiminus0forproton')
tuple.B0.PVFitpiminus0forproton.Verbose=True
tuple.B0.PVFitpiminus0forproton.constrainToOriginVertex=True
tuple.B0.PVFitpiminus0forproton.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiminus0forproton.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> ^pi- pi+ (pi0 -> gamma gamma))" : "p~-" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> ^pi+ pi- (pi0 -> gamma gamma))" : "p+" ,
    }
#==============================REFIT WITH ETA AND PV CONTRAINED - piplus -> Kminus swap ============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitpiplusforproton')
tuple.B0.PVFitpiplusforproton.Verbose=True
tuple.B0.PVFitpiplusforproton.constrainToOriginVertex=True
tuple.B0.PVFitpiplusforproton.daughtersToConstrain = ["eta"]
tuple.B0.PVFitpiplusforproton.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> pi- ^pi+ (pi0 -> gamma gamma))" : "p+" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> pi+ ^pi- (pi0 -> gamma gamma))" : "p~-" ,
    }

#==============================REFIT WITH ETA AND PV CONTRAINED - piplus -> Kminus swap ============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitgammaforpi0')
tuple.B0.PVFitgammaforpi0.Verbose=True
tuple.B0.PVFitgammaforpi0.constrainToOriginVertex=True
tuple.B0.PVFitgammaforpi0.daughtersToConstrain = ["eta"]
tuple.B0.PVFitgammaforpi0.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> pi- pi+ (pi0 -> ^gamma gamma))" : "pi0" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> pi+ pi- (pi0 -> ^gamma gamma))" : "pi0" ,
    }

#==============================REFIT WITH ETA AND PV CONTRAINED - piplus -> Kminus swap ============
tuple.B0.addTupleTool('TupleToolDecayTreeFitter/PVFitgamma0forpi0')
tuple.B0.PVFitgamma0forpi0.Verbose=True
tuple.B0.PVFitgamma0forpi0.constrainToOriginVertex=True
tuple.B0.PVFitgamma0forpi0.daughtersToConstrain = ["eta"]
tuple.B0.PVFitgamma0forpi0.Substitutions={
    "B0 -> (K*(892)0 ->  K+ pi-) (eta -> pi- pi+ (pi0 -> gamma ^gamma))" : "pi0" ,
    "B~0 -> (K*(892)~0 ->  K- pi+) (eta -> pi+ pi- (pi0 -> gamma ^gamma))" : "pi0" ,
    }



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

########################################=LOKI FUNCOR VARIABLES===============================================

tuple.addBranches({'Kstar' : '[B0 -> ^(K*(892)0 -> K+ pi-) (eta-> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'eta' : '[B0 -> (K*(892)0 -> K+ pi-) ^(eta-> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'Kplus' : '[B0 -> (K*(892)0 -> ^K+ pi-) (eta-> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'piminus' : '[B0 -> (K*(892)0 -> K+ ^pi-) (eta-> pi- pi+ (pi0 -> gamma gamma))]CC',
                   'piplus' : '[B0 -> (K*(892)0 -> K+ pi-) (eta-> pi- ^pi+ (pi0 -> gamma gamma))]CC',
                   'piminus0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta-> ^pi- pi+ (pi0 -> gamma gamma))]CC',
                   'gamma' : '[B0 -> (K*(892)0 -> K+ pi-) (eta-> pi- pi+ (pi0 -> ^gamma gamma))]CC',
                   'gamma0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta-> pi- pi+ (pi0 -> gamma ^gamma))]CC',
                   'pi0' : '[B0 -> (K*(892)0 -> K+ pi-) (eta-> pi- pi+ ^(pi0 -> gamma gamma))]CC'})

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
    'eta':'ETA'
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

gamma0_hybrid.Variables= {
    'eta':'ETA'
    }

pi0_hybrid.Variables={
    'eta':'ETA'
    }

#==============================MassSubs=====================================
from Configurables import TupleToolSubMass

tuple.B0.addTool(TupleToolSubMass)
tuple.B0.ToolList += ["TupleToolSubMass"]
tuple.B0.TupleToolSubMass.Substitution += ["pi- => K-"]
tuple.B0.TupleToolSubMass.Substitution += ["K+ => pi+"]
tuple.B0.TupleToolSubMass.Substitution += ["pi+ => K+"]
tuple.B0.TupleToolSubMass.Substitution += ["pi+ => p+"]
tuple.B0.TupleToolSubMass.Substitution += ["pi- => p~-"]
tuple.B0.TupleToolSubMass.Substitution += ["K+ => p+"]
tuple.B0.TupleToolSubMass.Substitution += ["gamma => pi0"]
tuple.B0.TupleToolSubMass.Substitution += ["gamma => e-"]
tuple.B0.TupleToolSubMass.Substitution += ["gamma => e+"]
tuple.B0.TupleToolSubMass.Substitution += ["pi- => mu-"]
tuple.B0.TupleToolSubMass.Substitution += ["pi+ => mu+"]
tuple.B0.TupleToolSubMass.Substitution += ["pi0 => eta"]
tuple.B0.TupleToolSubMass.DoubleSubstitution += ["K+/pi- => pi+/K-"]
tuple.B0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => pi-/pi+"]
tuple.B0.TupleToolSubMass.DoubleSubstitution += ["pi+/pi- => mu+/mu-"]


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


#from GaudiConf import IOHelper

# Use the local input data
#IOHelper().inputFiles([
 #   './00041836_00000057_1.bhadron.mdst'
  #  ], clear=True)





