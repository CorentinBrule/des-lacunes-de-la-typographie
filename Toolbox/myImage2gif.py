#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess
from ProgressBar import *
from PIL import Image,ImageSequence
from images2gif import writeGif
folderImages = sys.argv[1]
nameOutput = sys.argv[2]

maxWidth = 0
maxHeight = 0

imagesPath = os.listdir(folderImages)
images = []

for i in imagesPath :
    if ".png" in i :
        tmpImg = Image.open(folderImages+"/"+i)
        images.append(tmpImg)
        if tmpImg.size[0] > maxWidth : maxWidth = tmpImg.size[0]
        if tmpImg.size[1] > maxHeight : maxHeight = tmpImg.size[1]

imagesResized = []
tmpPaths = []

for i,img in enumerate(images) :
    tmpImg = Image.new('RGB',(maxWidth,maxHeight),'white')
    offset = ( round((maxWidth - img.size[0])/2) , round((maxHeight - img.size[1])/2) )
    tmpImg.paste(img,offset)
    tmpPath = folderImages + "/" + nameOutput + imagesPath[i]
    tmpPaths.append(tmpPath)
    tmpImg.save(tmpPath)
    #imagesResized.append(tmpImg)

subprocess.call(["convert" ,"-delay", "5","-loop","0", folderImages+nameOutput+"*" ,nameOutput+".gif"])
subprocess.call(["rm" , floderImages+nameOutput+*])

#writeGif(nameOutput,imagesResized,duration=1,dither=0)
