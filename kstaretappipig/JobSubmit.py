#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

polarity='MagDown'
datatype='MC'

b=Job()
b.application=DaVinci(version="v36r5")
if datatype=='MC':
    b.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
if datatype=='Data':
    b.application.optsfile='DNTupleMaker.py'
b.outputfiles=[DiracFile('Output.root')]
b.inputdata = b.application.readInputData('{0}_12_{1}_kstar_rho_kpipipi.py'.format(datatype,polarity))
b.comment='{0}_12_{1}_kstar_rho_kpipipi'.format(datatype,polarity)
b.splitter = SplitByFiles(filesPerJob=2)
#b.OutputSandbox=["stderr","stdout"]

b.backend=Dirac()
#b.submit()
queues.add(b.submit)
