from Gaudi.Configuration import *
from Configurables import DaVinci
from Configurables import GaudiSequencer

simulation=False

stream='Bhadron'
line='B2XEtaB2etapKstarLine'

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *
tuple=DecayTreeTuple()
tuple.Decay="[B0 -> ^(K*(892)0 -> ^K+ ^pi-) ^(eta_prime -> ^pi- ^pi+ ^gamma)]CC"
tuple.Branches={"B0":"[B0 -> (K*(892)0 -> K+ pi-) (eta_prime -> pi- pi+ gamma)]CC"}
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

from LoKiPhys.decorators import MAXTREE,MINTREE,ISBASIC,HASTRACK,SUMTREE,PT,ABSID,NINTREE,
B0_hybrid=tuple.B0.addTupleTool('LoKi::Hybrid::TupleTool/LoKi_B0')

preamble=[
    'TRACK_MAX_PT= MAXTREE(PT, ISBASIC & HASTRACK, -666)',
    'TRACK_MIN_PT= MINTREE(PT, ISBASIC & HASTRACK)',
    'SUMTRACK_PT= SUMTREE((211 == ABSID)|(-211 == ABSID)|(321 == ABSID)|(-321 == ABSID),PT)'
    ]
B0_hybrid.Preambulo=preamble

B0_hybrid.Variables = {
    'max_pt_track' : 'TRACK_MAX_PT',
    'min_pt_track' : 'TRACK_MIN_PT',
    'sum_track_pt' : 'SUMTRACK_PT',
    'n_highpt_tracks' : 'NINTREE(ISBASIC & HASTRACK & (PT>250.0*MeV))'
    }


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





