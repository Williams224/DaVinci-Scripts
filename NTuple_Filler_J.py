############################################ 
# DaVinci Options for filling ntuple with  #
# B0 -> KS0 (eta' -> pi pi gamma)          #
# for data or Monte Carlo                  #
############################################

from Gaudi.Configuration import *
from Configurables import DaVinci

#set your options for the job
simulation=True

#If its simulation, the monte carlo sample you are running on
sample='BdetapKs-pipig'
#If its data, the integrated luminosity from book-keeping
#2012
#lumi='1fb'
#2011: 480pb magup 600pb magdown
if(simulation):
    lumi="lumi"
else:
    lumi='1fb' #
mdst=True
dataType='2012'
magnet='magup'
stripping='stripping20r0p2'
sStream='Bhadron'
#Your stripping line (without the leading 'Stripping')
StrippingLine='B2XEtaB2etapKSDDLine'

head='B0'
daughter='etap'

#decay descriptor
#decay='[Lambda_b0 -> ^(eta_prime -> ^gamma ^pi+ ^pi-) ^(Lambda0 -> ^p+ ^pi-)]CC'
decay='B0 -> ^(eta_prime -> ^gamma ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-)'

print 'decay: '+decay

from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')

#Setting the output file names, the location for the tuple and the database tags if MC
if(simulation):
    name="MC"+dataType+"-"+magnet+"-"+sample+"-"+StrippingLine+"-"+stripping+"-filtered_"+trigger
    location="Phys/"+StrippingLine+"/Particles"
        
    DaVinci().DDDBtag='Sim08-20130503-1'
    DaVinci().CondDBtag='Sim08-20130503-1-vc-mu100'
else:
    name="data"+dataType+"-"+magnet+"-"+sample+"-"+sStream+"-"+StrippingLine+"-"+stripping+"-"+lumi
    location="/Event/"+sStream+"/Phys/"+StrippingLine+"/Particles"

if(mdst):
      

if(simulation):
    #######run stripping20 on MC11#################
    from StrippingConf.Configuration import StrippingConf, StrippingStream
    from StrippingSettings.Utils import strippingConfiguration
    from StrippingArchive.Utils import buildStreams
    from StrippingArchive import strippingArchive

    config=strippingConfiguration(stripping)
    archive=strippingArchive(stripping)
    streams=buildStreams(stripping=config,archive=archive)

    MyStream = StrippingStream("MyStream")
    MyLines = ["Stripping"+StrippingLine]

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
                      HDRLocation = "SomeNonExistingLocation") #only if running the same stripping again
                      
    DaVinci().appendToMainSequence([sc.sequence()])

#Creating the ntuple
from Configurables import DecayTreeTuple
from DecayTreeTuple.Configuration import *

tuple=DecayTreeTuple()
tuple.Inputs=[location]
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
    , "TupleToolTagging"
    ]
if(mdst!=True): tuple.ToolList+=["TupleToolTrackIsolation"]

tuple.Decay=decay

import re

brdecay=re.sub('\^','',decay)
print 'brdecay: '+brdecay


tuple.Branches={ "B0" : brdecay }

if(head=="B0"): 
elif(head=="Lb"):
    tuple.Branches={ "B0" : brdecay }
else:
    print "Unknown Head"
    
tuple.addTool(TupleToolDecay, name = "B0")

from Configurables import TupleToolDecayTreeFitter

tuple.B0.addTool(TupleToolDecayTreeFitter("PVFit"))
tuple.B0.PVFit.Verbose = True
tuple.B0.PVFit.constrainToOriginVertex = True

if(head=="B0"):
    if(daughter=="etap"):
        tuple.B0.PVFit.daughtersToConstrain = [ "eta_prime", "KS0" ]
    elif(daughter=="eta"):
        tuple.B0.PVFit.daughtersToConstrain = [ "eta", "KS0" ]
    else:
        Print("Unknown daughter")

elif(head=="Lb"):
    if(daughter=="etap"):
        tuple.B0.PVFit.daughtersToConstrain = [ "eta_prime", "Lambda0" ]
    elif(daughter=="eta"): 
        tuple.B0.PVFit.daughtersToConstrain = [ "eta", "Lambda0" ]
    else:
        print "Unknown Daughter"

else:
    print "Unkown Head"

tuple.B0.ToolList+=["TupleToolDecayTreeFitter/PVFit"]

from Configurables import TupleToolTISTOS
tistos = tuple.B0.addTupleTool(TupleToolTISTOS, name="TupleToolTISTOS")
tistos.VerboseL0=True
tistos.VerboseHlt1=True
tistos.VerboseHlt2=True
tistos.TriggerList=["L0PhotonDecision", "L0ElectronDecision", "Hlt1TrackPhotonDecision", "Hlt1TrackAllL0Decision","Hlt1TrackMuonDecision", "Hlt1TrackForwardPassThroughDecision","Hlt1TrackForwardPassThroughLooseDecision", "Hlt1SingleElectronNoIPDecision","L0HadronDecision","L0LocalPi0Decision","L0GlobalPi0Decision","L0MuonDecision","Hlt2Topo2BodyBBDTDecision","Hlt2Topo3BodyBBDTDecision","Hlt2Topo4BodyBBDTDecision", "Hlt2RadiativeTopoTrackTOSDecision", "Hlt2RadiativeTopoPhotonL0Decision","Hlt2TopoRad2BodyBBDTDecision","Hlt2TopoRad2plus1BodyBBDTDecision","Hlt2Topo2BodySimpleDecision","Hlt2Topo3BodySimpleDecision","Hlt2Topo4BodySimpleDecision"]

if(simulation):
    etuple=EventTuple()
    etuple.ToolList=["TupleToolEventInfo"]

    MySequencer.Members.append(etuple)
    
    from Configurables import MCDecayTreeTuple
    mctuple=MCDecayTreeTuple()
    mctuple.ToolList+=["MCTupleToolKinematic","MCTupleToolReconstructed","MCTupleToolHierarchy","MCTupleToolDecayType","MCTupleToolPID"]

    if(head=="B0"):
        decay2=re.sub('\^\(\KS0 \-\> \^pi\+ \^pi\-\)','^KS0',decay)
        mcdecay=re.sub('\)',' {,gamma}{,gamma}{,gamma}{,gamma})',decay2)      
        mcdecay = '['+mcdecay+']cc'
    elif(head=="Lb"):
        decay2=re.sub('\^\(Lambda0 \-\> \^p\+ \^pi\-\)','^Lambda0',decay)
        mcdecay=re.sub('\)',' {,gamma}{,gamma}{,gamma}{,gamma})',decay2) 

    print 'mcdecay= '+mcdecay

    mctuple.Decay=mcdecay    

MySequencer.Members.append(tuple)

if(mdst):
    DaVinci().InputType='MDST'
    DaVinci().UserAlgorithms+=[MySequencer]    
else:
    DaVinci().InputType='DST'
    DaVinci().UserAlgorithms+=[MySequencer]

DaVinci().TupleFile=name+".root"
DaVinci().HistogramFile=name+"-histos.root"
DaVinci().DataType=dataType
DaVinci().EvtMax=500
DaVinci().PrintFreq=1000
DaVinci().MoniSequence=[tuple]
DaVinci().Simulation=simulation
