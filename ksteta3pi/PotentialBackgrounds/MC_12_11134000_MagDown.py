#-- GAUDI jobOptions generated on Fri Jul 24 16:50:08 2015
#-- Contains event types : 
#--   11134000 - 36 files - 514427 events - 111.75 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-124834 

#--  StepId : 124834 
#--  StepName : Reco14a for MC 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v43r2p7 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/DataType-2012.py;$APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-124620 

#--  StepId : 124620 
#--  StepName : Digi13 with G4 dE/dx 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v26r3 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/DataType-2012.py;$APPCONFIGOPTS/Boole/Boole-SiG4EnergyDeposit.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-126567 

#--  StepId : 126567 
#--  StepName : Sim08e - 2012 - MD - Pythia8 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v45r7 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Sim08-Beam4000GeV-md100-2012-nu2.5.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIA8ROOT/options/Pythia8.py;$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20130929-1 
#--  CONDDB : sim-20130522-1-vc-md100 
#--  ExtraPackages : AppConfig.v3r193;DecFiles.v27r24 
#--  Visible : Y 


#--  Processing Pass Step-124632 

#--  StepId : 124632 
#--  StepName : TCK-0x409f0045 Flagged for Sim08 2012 
#--  ApplicationName : Moore 
#--  ApplicationVersion : v14r8p1 
#--  OptionFiles : $APPCONFIGOPTS/Moore/MooreSimProductionWithL0Emulation.py;$APPCONFIGOPTS/Conditions/TCK-0x409f0045.py;$APPCONFIGOPTS/Moore/DataType-2012.py;$APPCONFIGOPTS/L0/L0TCK-0x0045.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 


#--  Processing Pass Step-124630 

#--  StepId : 124630 
#--  StepName : Stripping20-NoPrescalingFlagged for Sim08 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000001_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000002_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000003_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000004_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000005_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000006_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000007_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000008_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000009_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000010_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000011_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000012_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000013_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000014_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000015_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000016_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000017_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000018_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000019_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000020_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000021_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000022_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000023_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000024_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000025_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000026_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000027_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000028_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000029_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000030_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000031_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000032_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000033_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000034_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000035_1.allstreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00037025/0000/00037025_00000036_1.allstreams.dst'
], clear=True)
