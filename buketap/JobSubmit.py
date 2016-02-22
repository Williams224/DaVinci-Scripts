#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

polarity='MagDown'
datatype='Data'
channel='buketap'
year='12'

b=Job()
b.application=DaVinci(version="v36r5")
if datatype=='MC':
    b.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
if datatype=='Data':
    b.application.optsfile='DNTupleMaker.py'
b.outputfiles=[DiracFile('Output.root')]
print '{0}_{1}_{2}_{3}.py'.format(datatype,year,polarity,channel)
b.inputdata = b.application.readInputData('{0}_{1}_{2}_{3}.py'.format(datatype,year,polarity,channel))
b.comment='{0}_{1}_{2}_{3}_EPFLFixed'.format(datatype,year,polarity,channel)
if datatype=='Data':
    b.splitter = SplitByFiles(filesPerJob=10)
if datatype=='MC':
    b.splitter = SplitByFiles(filesPerJob=2)

#b.OutputSandbox=["stderr","stdout"]
b.backend=Dirac()
#b.submit()
queues.add(b.submit)

polarity='MagUp'

b2=Job()
b2.application=DaVinci(version="v36r5")
if datatype=='MC':
    b2.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
if datatype=='Data':
    b2.application.optsfile='DNTupleMaker.py'
b2.outputfiles=[DiracFile('Output.root')]
b2.inputdata = b2.application.readInputData('{0}_{1}_{2}_{3}.py'.format(datatype,year,polarity,channel))
b2.comment='{0}_{1}_{2}_{3}_EPFLFixedg'.format(datatype,year,polarity,channel)
if datatype=='Data':
    b2.splitter = SplitByFiles(filesPerJob=10)
if datatype=='MC':
    b2.splitter = SplitByFiles(filesPerJob=2)

#b2.OutputSandbox=["stderr","stdout"]

b2.backend=Dirac()
queues.add(b2.submit)
