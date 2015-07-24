#!/usr/bin/env ganga

import getpass
from distutils.util import strtobool
import os
import re
DoneBkgs=['nobkg']
for fname in os.listdir("./PotentialBackgrounds"):
    channel=fname[6:14]
    if re.search("MC_12_1.*py",fname)>0 and not channel in DoneBkgs:
        DoneBkgs.append(channel)
        print fname
        polarity='MagDown'
        datatype='MC'
        substitution='None'
        
        

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
        b.inputdata = b.application.readInputData('PotentialBackgrounds/{0}_12_{1}_{2}.py'.format(datatype,channel,polarity))
        if substitution=='None':
            b.comment='{0}_12_{1}_{2}'.format(datatype,polarity,channel)
        if substitution=='PimforKm':
            b.comment='{0}_12_{1}_{2}_{3}'.format(datatype,polarity,channel,substitution)
        if datatype=='Data':
            b.splitter = SplitByFiles(filesPerJob=10)
        if datatype=='MC':
            b.splitter = SplitByFiles(filesPerJob=2)
        b.backend=Dirac()
        b.postprocessors.append(RootMerger(files = ['Output.root'],ignorefailed = False,overwrite = True))
        queues.add(b.submit)
        if channel!='11144203':
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
            b2.inputdata = b2.application.readInputData('PotentialBackgrounds/{0}_12_{1}_{2}.py.py'.format(datatype,channel,polarity))
            if substitution=='None':
                b2.comment='{0}_12_{1}_{2}'.format(datatype,polarity,channel)
            if substitution=='PimforKm':
                b2.comment='{0}_12_{1}_{2}_{3}'.format(datatype,polarity,channel,substitution)
            if datatype=='Data':
                b2.splitter = SplitByFiles(filesPerJob=10)
            if datatype=='MC':
                b2.splitter = SplitByFiles(filesPerJob=2)
                

            b2.backend=Dirac()
            b2.postprocessors.append(RootMerger(files = ['Output.root'],ignorefailed = False,overwrite = True))
                    
            queues.add(b2.submit)
