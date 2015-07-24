#-- GAUDI jobOptions generated on Fri Jul 17 16:37:45 2015
#-- Contains event types : 
#--   11104101 - 106 files - 2116085 events - 602.40 GBytes


#--  Extra information about the data processing phases:

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000001_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000002_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000003_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000004_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000005_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000006_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000007_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000008_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000009_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000010_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000011_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000012_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000013_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000014_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000015_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000016_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000017_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000019_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000020_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000021_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000022_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000023_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000024_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000025_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000055_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000056_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000057_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000058_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000059_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000060_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000061_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000062_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000063_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000065_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000066_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000068_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000070_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000073_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000075_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000077_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000079_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000082_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000086_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000090_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000092_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000093_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000096_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000099_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000100_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000101_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000102_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000103_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000104_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000105_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000106_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000107_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000108_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000109_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000110_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000111_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000112_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000113_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000114_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000115_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000116_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000117_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000118_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000119_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000120_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000121_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000122_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000123_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000124_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000125_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000126_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000127_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000128_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000129_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000130_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000131_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000132_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000133_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000134_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000135_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000136_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000137_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000138_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000139_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000140_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000141_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000142_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000143_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000144_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000145_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000146_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000147_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000148_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000149_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000150_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000151_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000152_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000153_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000154_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000155_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000156_2.AllStreams.dst',
'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00041907/0000/00041907_00000157_2.AllStreams.dst'
], clear=True)
