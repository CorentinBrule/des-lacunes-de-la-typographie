#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
rootFolder=sys.argv[1]
listRootFolder=os.listdir(rootFolder)

Bar1 = ProgressBar(len(listRootFolder), 30 , "Sort unsorted images (Step 1/2)")
for imgUnsorted in listRootFolder:
     Bar1.update()
     if re.findall('.png', imgUnsorted):
         glyphName=imgUnsorted[0]
         if glyphName==".":
             subprocess.call(["mkdir","-p",rootFolder+".point"])
             subprocess.call(["mv",rootFolder+imgUnsorted,rootFolder+".point/"])
         else :
             subprocess.call(["mkdir","-p",rootFolder+glyphName])
             subprocess.call(["mv",rootFolder+imgUnsorted,rootFolder+glyphName])

totalFile=0
nbfolder=0
for r,d,f in os.walk(rootFolder):
    nbfolder+=1
    for i in f:
         totalFile+=1
totalFile-=nbfolder
Bar2 = ProgressBar(nbfolder, 30 , "Resort "+str(totalFile)+" sorted images (Step 2/2)")

for folder in listRootFolder:
    if not re.findall('.png', folder):
        if "autre" not in folder:
            for imgSorted in os.listdir(rootFolder+folder):
                Bar2.update()
                if re.findall('.png', imgSorted):
                    glyphName=imgSorted[0]
                    if glyphName==".":
                        if folder!=".point":
                            subprocess.call(["mv",rootFolder+folder+"/"+imgSorted,rootFolder+".point/"+imgSorted])

                    elif glyphName!=folder:
                        imgSortedBad=imgSorted
                        imgSortedGood=imgSortedBad.replace(glyphName,folder,1)

                        subprocess.call(["mv",rootFolder+folder+"/"+imgSortedBad,rootFolder+folder+"/"+imgSortedGood])

                        #subprocess.call(["mv",rootFolder+folder+"/"+imgSorted,rootFolder+glyphName+"/"+imgSorted])
