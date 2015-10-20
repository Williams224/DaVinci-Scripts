#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool

polarity='MagDown'
datatype='Data'
substitution='None'
channel='kstar_eta_3pi'


b=Job()
b.application=DaVinci(version="v36r5")
if datatype=='MC':
    b.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
if datatype=='Data':
    if substitution=='None':
        b.application.optsfile='DNTupleMaker.py'
    if substitution=='PimforKm':
        b.application.optsfile='DNTupleMaker_PimforKm.py'
b.outputfiles=[DiracFile('Output.root')]
print '{0}_12_{1}_{2}.py'.format(datatype,polarity,channel)
b.inputdata = b.application.readInputData('{0}_12_{1}_{2}.py'.format(datatype,polarity,channel))
if substitution=='None':
    b.comment='{0}_12_{1}_{2}'.format(datatype,polarity,channel)
if substitution=='PimforKm':
    b.comment='{0}_12_{1}_{2}_{3}'.format(datatype,polarity,channel,substitution)
if datatype=='Data':
        b.splitter = SplitByFiles(filesPerJob=10)
if datatype=='MC':
    b.splitter = SplitByFiles(filesPerJob=2)
b2.OutputSandbox=["stderr","stdout"]

b.backend=Dirac()
#b.submit()
queues.add(b.submit)

polarity='MagUp'

b2=Job()
b2.application=DaVinci(version="v36r5")
if datatype=='MC':
    b2.application.optsfile='NTupleMaker_{0}.py'.format(polarity)
if datatype=='Data':
    if substitution=='None':
        b2.application.optsfile='DNTupleMaker.py'
    if substitution=='PimforKm':
        b2.application.optsfile='DNTupleMaker_PimforKm.py'
b2.outputfiles=[DiracFile('Output.root')]
b2.inputdata = b2.application.readInputData('{0}_12_{1}_{2}.py'.format(datatype,polarity,channel))
if substitution=='None':
    b2.comment='{0}_12_{1}_{2}'.format(datatype,polarity,channel)
if substitution=='PimforKm':
    b2.comment='{0}_12_{1}_{2}_{3}'.format(datatype,polarity,channel,substitution)
if datatype=='Data':
    b2.splitter = SplitByFiles(filesPerJob=10)
if datatype=='MC':
    b2.splitter = SplitByFiles(filesPerJob=2)
b2.OutputSandbox=["stderr","stdout"]

b2.backend=Dirac()
#b.submit()
queues.add(b2.submit)
