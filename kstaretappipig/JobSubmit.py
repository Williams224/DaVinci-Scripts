#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

polarity='MagDown'

b=Job()
b.application=DaVinci(version="v36r5")
b.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
b.outputfiles=[DiracFile('Output.root')]
b.inputdata = b.application.readInputData('MC_12_{0}_Kstar_etap_pipig.py'.format(polarity))
b.comment='MC_12_{0}_kstar_etap_pipig'.format(polarity)
b.splitter = SplitByFiles(filesPerJob=2)
#b.OutputSandbox=["stderr","stdout"]

b.backend=Dirac()
#b.submit()
queues.add(b.submit)
