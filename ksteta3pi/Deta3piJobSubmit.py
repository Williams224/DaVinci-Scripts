#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

b=Job()
b.application=DaVinci(version='v36r5')
b.application.optsfile='DNTupleMaker.py'
b.outputfiles=[DiracFile('Output.root')]
b.inputdata=browseBK()
b.splitter = SplitByFiles(filesPerJob=100)
com=raw_input('Enter Comment for this job: ')
b.comment=com
#b.OutputSandbox=["stderr","stdout"]

b.backend=Dirac()
queues.add(b.submit)
