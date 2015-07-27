#-- GAUDI jobOptions generated on Fri Jul 17 16:45:18 2015
#-- Contains event types : 
#--   11104601 - 17 files - 271334 events - 79.15 GBytes


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
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000016_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000017_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000018_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000019_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000020_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041903/0000/00041903_00000021_2.AllStreams.dst'
], clear=True)
