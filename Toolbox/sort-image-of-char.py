#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
rootFolder = sys.argv[1]
listRootFolder = os.listdir(rootFolder) #list of the elements in the root folder

# Step one : sort unsorted images wich are in the root folder
Bar1 = ProgressBar(len(listRootFolder), 30 , "Sort unsorted images (Step 1/2)")
for imgUnsorted in listRootFolder:
     Bar1.update()
     if re.findall('.png', imgUnsorted): #if this element is an image :
         #get the char name of the glyph
         glyphName=imgUnsorted[0]
         #create dir if it's necessary, move the image in this dir
         if glyphName == ".": #to fix "." name
             subprocess.call(["mkdir","-p",rootFolder+".point"])
             subprocess.call(["mv",rootFolder+imgUnsorted,rootFolder+".point/"])
         else :
             subprocess.call(["mkdir","-p",rootFolder+glyphName])
             subprocess.call(["mv",rootFolder+imgUnsorted,rootFolder+glyphName])

# Step two : rename file if it does not correspond with the name of the folder in which it is.
# prepares the estimation of the process time.
totalFile=0
nbfolder=0
for r,d,f in os.walk(rootFolder):
    nbfolder+=1
    for i in f:
         totalFile+=1
totalFile-=nbfolder
Bar2 = ProgressBar(nbfolder, 30 , "Resort "+str(totalFile)+" sorted images (Step 2/2)")

for folder in listRootFolder:
    if not re.findall('.png', folder): #found folders (not png files)
        if "autre" not in folder: #Fix the ambiguous glyphs by hand by calling them "autre".
            for imgSorted in os.listdir(rootFolder+folder):
                Bar2.update()
                if re.findall('.png', imgSorted):
                    glyphName=imgSorted[0]
                    if glyphName==".": #fix "." name
                        if folder!=".point":
                            subprocess.call(["mv",rootFolder+folder+"/"+imgSorted,rootFolder+".point/"+imgSorted])

                    elif glyphName!=folder:
                        imgSortedBad=imgSorted
                        imgSortedGood=imgSortedBad.replace(glyphName,folder,1)

                        subprocess.call(["mv",rootFolder+folder+"/"+imgSortedBad,rootFolder+folder+"/"+imgSortedGood])

                        #subprocess.call(["mv",rootFolder+folder+"/"+imgSorted,rootFolder+glyphName+"/"+imgSorted])
