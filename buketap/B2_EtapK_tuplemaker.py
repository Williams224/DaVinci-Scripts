#!/usr/bin/env python
# =============================================================================
# @file
# @author   rita giani (sebastiana.giani@epfl.ch)
# @date     2015-02-23
# =============================================================================

from Gaudi.Configuration           import *
from Configurables                 import DaVinci, PrintDecayTree, GaudiSequencer,SubstitutePID,TupleToolTISTOS
from Configurables                 import LoKi__HDRFilter, LoKi__VoidFilter
from PhysSelPython.Wrappers        import AutomaticData, Selection, SelectionSequence, MergedSelection
from Configurables                 import FilterDesktop
from Configurables                 import DecayTreeTuple, TupleToolTrigger, TupleTool
from StrippingConf.StrippingLine   import *
from StrippingConf.Configuration   import *
from StrippingConf.StrippingStream import StrippingStream
from StrippingArchive              import strippingArchive
from StrippingArchive.Utils        import buildStreams
from StrippingSettings.Utils       import strippingConfiguration
from Configurables                 import TESCheck
from Configurables import LoKi__Hybrid__TupleTool
from Configurables          import CombineParticles

from Configurables import FilterInTrees

#Stripping 21 3 body#

line='BetaSQ2B3piSelectionLine'
location = '/Event/Phys/'+line+'/Particles'


# List of Trigger decisions to include in TISTOS
HltLines = {   'L0'   : ["Hadron","Photon","Muon","Electron"],
                'Hlt1' : ['TrackAllL0'],
                'Hlt2' : ['Topo2BodyBBDT', 'Topo3BodyBBDT','Topo4BodyBBDT'] }

myTriggerList = []
for stage, lines in HltLines.iteritems():
    for line in lines: myTriggerList.append( stage+line+'Decision' )



#kill the previous stripping just in case (it is not the case) your file was already stripped.
from Configurables import EventNodeKiller
killer = EventNodeKiller('Stripkiller')
killer.Nodes = ['/Event/AllStreams', '/Event/Strip']



stripping='stripping20r0p2'
config  = strippingConfiguration(stripping)
archive = strippingArchive(stripping)
streams = buildStreams(stripping=config, archive=archive)



# Select my line
MyStream = StrippingStream("MyStream")
MyLines = ['StrippingBetaSQ2B3piSelectionLine']

for stream in streams: 
    for line in stream.lines:
        if line.name() in MyLines:
            MyStream.appendLines( [ line ] ) 


# Configure Stripping
from Configurables import ProcStatusCheck
filterBadEvents = ProcStatusCheck()

sc = StrippingConf( Streams = [ MyStream ],
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = filterBadEvents )


from Configurables import StrippingReport
sr = StrippingReport(Selections = sc.selections());

MySequencer = GaudiSequencer('Sequence')
MySequencer.Members = [sc.sequence(),sr]
MySequencer.IgnoreFilterPassed = True 

DaVinci().appendToMainSequence([killer, MySequencer])


 
from Configurables import FilterInTrees

rho_list = FilterInTrees( 'rho_list', Code = "'rho(770)0'==ABSID")
rho_Sel = Selection ( "rho_Sel" , Algorithm =rho_list  , RequiredSelections = [ AutomaticData(Location = location) ] )
rho_Seq = SelectionSequence("rho_Seq", TopSelection = rho_Sel)



 
pion_list= FilterInTrees( 'pion_list', Code = "'pi+'==ABSID")   
pion_Sel = Selection ( "pion_Sel" , Algorithm =pion_list  , RequiredSelections = [ AutomaticData(Location = location)  ] )
pion_Seq = SelectionSequence("pion_Seq", TopSelection = pion_Sel)




from StandardParticles import StdLooseAllPhotons


PhotonFilter = FilterDesktop("PhotonFilter", Code="(PT > 300.*MeV) & (CL > 0.1)")
PhotonSel    = Selection('PhotonSel', Algorithm=PhotonFilter, RequiredSelections=[StdLooseAllPhotons])



my_etap = CombineParticles("my_etap")
my_etap.DecayDescriptor = "eta_prime -> rho(770)0 gamma"
my_etap.MotherCut = "(ADMASS('eta_prime') < 100.*MeV)" # & (PT > 1500.*MeV) & (P > 4000.*MeV) " #& (VFASPF(VCHI2/VDOF) < 9.)" #   "ALL" #  
my_etap_Sel = Selection("my_etap_Sel", 
                            Algorithm = my_etap, 
                          # RequiredSelections = [rho_Sel,StdLooseAllPhotons]) 
                            RequiredSelections = [rho_Sel,PhotonSel])
#my_etap_Seq = SelectionSequence("my_etap_Seq", TopSelection = my_etap_Sel)



preambulo=[
"rho_px= CHILD (PX,1,1 ) " ,
"rho_py=CHILD  (PY,1,1 )" ,
"rho_pz=CHILD (PZ,1,1 ) ",
"rho_E= CHILD (E,1,1 ) " ,
"pi_px= CHILD (PX,2 ) " ,
"pi_py= CHILD (PY,2 ) " ,
"pi_pz= CHILD (PZ,2 ) " ,
"pi_E= CHILD (E,2) " ,
"pi_PT=CHILD (PT,2) " ,
"rhopi_px=  rho_px + pi_px",
"rhopi_py=  rho_py + pi_py",
"rhopi_pz=  rho_pz + pi_pz",
"rhopi_E=   rho_E  + pi_E",
"IM_rhopi = sqrt(rhopi_E**2 - rhopi_px**2 - rhopi_py**2 - rhopi_pz**2)"
]


# Create B candidate
B2etap_pi = CombineParticles("B2etap_pi",Preambulo=preambulo)
B2etap_pi.DecayDescriptors = ['[B+ -> eta_prime pi+]cc' ]
B2etap_pi.MotherCut ="(IM_rhopi>4200) & (IM_rhopi<6700) & (pi_PT>1000)" 
B2etap_piSub = Selection("B2etap_piSub", Algorithm = B2etap_pi, RequiredSelections = [my_etap_Sel,pion_Sel])
B2etap_piSeq = SelectionSequence("B2etap_piSeq", TopSelection =B2etap_piSub)


#pt = PrintDecayTree(Inputs = [B2rhopiSeq.outputLocation()])


#SubPID

SubKToPi = SubstitutePID ( name = 'SubKToPi', 
                            Code = " DECTREE('[(B+ -> eta_prime pi+),(B- -> eta_prime pi-) ]') " , 
                            Substitutions = { 
                                'B+ -> eta_prime  ^pi+'  : 'K+', 
                                'B- -> eta_prime  ^pi-'  : 'K-',
                            }
)
                         

B2EtapKSel = Selection("B2EtapKSel", Algorithm = SubKToPi, RequiredSelections = [B2etap_piSub])

#B2EtapKSeq = SelectionSequence("B2EtapKSeq", TopSelection = B2EtapKSel)

#Code="(M>4800 *MeV) & (M<5700 *MeV) & (VFASPF(VCHI2/VDOF)<9.) & (PT> 1500.*MeV)"
B2EtapKFil= FilterDesktop("B2EtapKFil",  Code="(M>4800 *MeV) & (M<5700 *MeV) & (VFASPF(VCHI2/VDOF)<9.)")# & (PT> 1500.*MeV)") 
B2EtapKFil_Sel= Selection('B2EtapKFil_Sel', Algorithm=B2EtapKFil, RequiredSelections=[B2EtapKSel])
B2EtapKFil_Seq = SelectionSequence("B2etap_pi_FilSeq", TopSelection =B2EtapKFil_Sel) 




# Fill Tuple
from Configurables import DecayTreeTuple

tuple = DecayTreeTuple("B2_ETAPK")

 
tuple.ToolList += [
       "TupleToolGeometry",
       "TupleToolPhotonInfo",
       "TupleToolPid",
       "TupleToolMCTruth",
       "TupleToolRICHPid",
       "TupleToolKinematic",
       "TupleToolPrimaries",
       "TupleToolEventInfo",
       "TupleToolTrackInfo",
       "TupleToolAngles",
       "TupleToolPropertime",
       "TupleToolVtxIsoln",
        "TupleToolMCBackgroundInfo"
        ]



decay="[B+ -> ^(eta_prime -> ^(rho(770)0 -> ^pi+ ^pi-) ^gamma ) ^K+]CC"
tuple.Decay =decay


#DecayTreeFitter Tool
tuple.Branches = { 'B'  : "^("+decay.replace("^","")+")" }
from Configurables import TupleToolDecay
tuple.addTool(TupleToolDecay, name = 'B')

tuple.B.ToolList+=["TupleToolTISTOS"]
tuple.B.addTool( TupleToolTISTOS , name="TupleToolTISTOS")
tuple.B.TupleToolTISTOS.VerboseHlt1 = True
tuple.B.TupleToolTISTOS.VerboseHlt2 = True
tuple.B.TupleToolTISTOS.VerboseL0 = True
tuple.B.TupleToolTISTOS.TriggerList = myTriggerList

from Configurables import TupleToolDecayTreeFitter
tuple.B.ToolList +=  ["TupleToolDecayTreeFitter/MassFit",
                     ]         # fit with eta_prime mass onstraint
tuple.B.addTool(TupleToolDecayTreeFitter,name="MassFit")
tuple.B.MassFit.constrainToOriginVertex = False
tuple.B.MassFit.daughtersToConstrain = [ "eta_prime" ]
tuple.B.MassFit.Verbose = True
tuple.B.MassFit.UpdateDaughters = True



tuple.Inputs= [B2EtapKFil_Seq.outputLocation()]

DaVinci().InputType = 'DST'
# MC 2012
DaVinci().DDDBtag =  "dddb-20130929-1"
DaVinci().CondDBtag= "sim-20130522-1-vc-md100"
DaVinci().DataType = "2012"
DaVinci().EvtMax = 10000
DaVinci().PrintFreq = 10000
DaVinci().HistogramFile = "DVHistos.root"
DaVinci().Simulation = True
DaVinci().TupleFile = "B2ETAPK_MC.root"
DaVinci().appendToMainSequence([B2EtapKFil_Seq,tuple])


from GaudiConf import IOHelper
# Use the local input data
IOHelper().inputFiles([
        './MC_12_12103211.dst'
], clear=True)

#EventSelector().Input = [
                         
                         
#                         "DATAFILE='PFN:/panfs/fblanc/data/00025869_00000002_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/fblanc/data/00025869_00000003_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/fblanc/data/00025869_00000004_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/segiani/EtapK_data/00025869_00000005_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/segiani/EtapK_data/00025869_00000006_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/segiani/EtapK_data/00025869_00000007_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'",
#                         "DATAFILE='PFN:/panfs/segiani/EtapK_data/00025869_00000008_1.allstreams.dst' TYP='POOL_ROOTTREE' OPT='READ'"
#                          ]



#EOF
