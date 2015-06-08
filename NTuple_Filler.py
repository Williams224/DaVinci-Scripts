# This is taken from the following sources
# https://www.ep.ph.bham.ac.uk/twiki/bin/view/General/DaVinci
# https://twiki.cern.ch/twiki/bin/view/LHCb/StrippingFAQ

from Gaudi.Configuration import *
from Configurables import GaudiSequencer
from Configurables import DaVinci

# Just some little self configuration
simulation = True


################################################################################
# This bit is if you need to change the stripping line applied to the MC

if simulation:
    from StrippingConf.Configuration import StrippingConf, StrippingStream
    from StrippingSettings.Utils import strippingConfiguration
    from StrippingArchive.Utils import buildStreams
    from StrippingArchive import strippingArchive

    stripping="stripping21"
    config=strippingConfiguration(stripping)
    archive=strippingArchive(stripping)
    streams=buildStreams(stripping=config,archive=archive)

    MyStream = StrippingStream("MyStream")
    MyLines = ["StrippingBc2KstKBc2XK"]

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

    DaVinci().appendToMainSequence( [ sc.sequence() ] )


#
################################################################################

from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *

my_tuple = DecayTreeTuple("BcDecayTreeTuple") 
if simulation:
    my_tuple.Inputs = ["/Phys/Bc2KstKBc2XK/Particles"]
else:
    my_tuple.Inputs = ["/Event/Bhadron/Phys/Bc2KstKBc2XK/Particles"]
my_tuple.Decay="[B_c+ -> ^(K*(892)~0 -> ^K- ^pi+) ^K+]CC"
my_tuple.Branches={"B_c+":"[B_c+ -> (K*(892)~0 -> K- pi+) K+]CC" }
my_tuple.addTool( TupleToolDecay, name = "Bc" )

my_tuple.ToolList += [
    "TupleToolGeometry",
    "TupleToolDira",
    "TupleToolAngles",
    "TupleToolPid",
    "TupleToolKinematic",
    "TupleToolPropertime",
    "TupleToolPrimaries",
    "TupleToolEventInfo",
    "TupleToolTrackInfo",
    "TupleToolVtxIsoln",
    "TupleToolPhotonInfo",
    "TupleToolCaloHypo"
    # "TupleToolTagging" # Not contained in MDST
    ]

if simulation:
    my_tuple.ToolList += [
        "TupleToolMCTruth",
        "TupleToolMCBackgroundInfo",
        ]

from Configurables import TupleToolTISTOS
tistos = my_tuple.Bc.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
tistos.VerboseL0=True
tistos.VerboseHlt1=True
tistos.VerboseHlt2=True
tistos.TriggerList=["L0PhotonDecision",
                    "L0ElectronDecision",
                    "Hlt1TrackAllL0Decision",
                    "Hlt2Topo2BodyBBDTDecision"]



etuple=EventTuple()
etuple.ToolList=["TupleToolEventInfo"] 


# killing those event nodes for MDST compatibility
seq = GaudiSequencer('EventKillerSeq')
from Configurables import EventNodeKiller
eventNodeKiller = EventNodeKiller('DAQkiller')
eventNodeKiller.Nodes = ['DAQ','pRec']
seq.Members+=[eventNodeKiller] 

DaVinci().InputType='MDST'
DaVinci().TupleFile="davinci.root"
DaVinci().HistogramFile="davinci-histos.root"
DaVinci().DataType="2012"
# DaVinci().EvtMax=2000
DaVinci().EvtMax=-1
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[ my_tuple ]
DaVinci().UserAlgorithms = [
    seq,
    my_tuple,
    etuple,
    ]

if simulation:
    DaVinci().Simulation=True
    DaVinci().DDDBtag='MC11-20111102'
    DaVinci().CondDBtag='sim-20111111-vc-mu100' 
else:
    DaVinci().Simulation=False
