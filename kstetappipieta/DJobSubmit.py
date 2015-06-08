#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

b=Job()
b.application=DaVinci()
b.application.optsfile='DNTupleMaker.py'
b.outputfiles=[DiracFile('Output.root')]
b.inputdata=browseBK()
b.splitter = SplitByFiles(filesPerJob=50)
b.backend=Dirac()
queues.add(b.submit)
