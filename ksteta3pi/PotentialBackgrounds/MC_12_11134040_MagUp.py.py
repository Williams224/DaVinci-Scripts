#-- GAUDI jobOptions generated on Fri Jul 24 16:54:59 2015
#-- Contains event types : 
#--   11134040 - 16 files - 276695 events - 80.09 GBytes


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
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000003_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000004_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000005_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000006_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00043187/0000/00043187_00000016_2.AllStreams.dst'
], clear=True)
