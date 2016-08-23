#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re

rootFolder=sys.argv[1]

for cU in os.listdir(rootFolder):
     if re.findall('.png', cU):
         gN=cU[0]
         subprocess.call(["mkdir","-p",rootFolder+gN])
         subprocess.call(["mv",rootFolder+cU,rootFolder+gN])

for folder in os.listdir(rootFolder):
    if not re.findall('.png', folder):
        for cS in os.listdir(rootFolder+folder):
            if re.findall('.png', cS):
                gN=cS[0]
                if gN!=folder:
                    print("différent!:"+rootFolder+folder+"/"+cS)
                    subprocess.call(["mv",rootFolder+folder+"/"+cS,rootFolder+gN+"/"+cS])
