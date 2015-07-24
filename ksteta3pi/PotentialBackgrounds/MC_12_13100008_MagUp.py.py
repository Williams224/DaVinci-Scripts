#-- GAUDI jobOptions generated on Fri Jul 24 17:14:59 2015
#-- Contains event types : 
#--   13100008 - 98 files - 2062195 events - 558.40 GBytes


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


#--  Processing Pass Step-125836 

#--  StepId : 125836 
#--  StepName : Stripping20-NoPrescalingFlagged for Sim08 - Implicit merging. 
#--  ApplicationName : DaVinci 
#--  ApplicationVersion : v32r2p1 
#--  OptionFiles : $APPCONFIGOPTS/DaVinci/DV-Stripping20-Stripping-MC-NoPrescaling.py;$APPCONFIGOPTS/DaVinci/DataType-2012.py;$APPCONFIGOPTS/DaVinci/InputType-DST.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r164 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000003_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000004_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000005_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000006_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000016_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000017_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000018_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000019_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000020_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000021_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000022_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000023_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000024_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000025_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000026_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000027_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000028_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000029_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000030_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000031_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000032_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000033_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000034_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000035_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000036_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000037_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000038_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000039_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000040_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000041_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000042_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000043_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000044_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000045_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000046_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000047_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000048_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000049_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000050_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000051_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000052_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000053_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000054_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000055_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000056_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000057_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000058_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000059_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000060_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000061_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000062_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000063_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000064_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000065_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000066_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000067_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000068_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000069_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000070_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000071_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000072_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000073_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000074_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000075_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000076_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000077_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000078_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000079_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000080_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000081_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000082_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000083_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000084_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000085_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000086_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000087_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000088_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000089_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000090_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000091_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000092_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000093_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000094_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000095_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000096_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000097_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00042454/0000/00042454_00000098_2.AllStreams.dst'
], clear=True)
