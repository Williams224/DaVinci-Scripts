#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

b=Job()
b.application=DaVinci(version="v36r5")
b.application.optsfile='NTupleMaker.py'
b.outputfiles=[DiracFile('Output.root')]
b.inputdata=browseBK()
b.splitter = SplitByFiles(filesPerJob=10)
#b.OutputSandbox=["stderr","stdout"]

b.backend=Dirac()
#b.submit()
queues.add(b.submit)
