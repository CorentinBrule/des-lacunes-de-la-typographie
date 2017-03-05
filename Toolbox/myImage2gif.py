#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess
from ProgressBar import *
from PIL import Image,ImageSequence
from images2gif import writeGif
folderImages = sys.argv[1]
#nameOutput = sys.argv[2]
char = folderImages.split('/')[-2]

maxWidth = 0
maxHeight = 0

imagesPath = os.listdir(folderImages)

images = {}
for i in imagesPath :
    if ".png" in i :
        tmpImg = Image.open(folderImages+"/"+i)
        images[i]=tmpImg
        if tmpImg.size[0] > maxWidth : maxWidth = tmpImg.size[0]
        if tmpImg.size[1] > maxHeight : maxHeight = tmpImg.size[1]

imagesResized = []
tmpPaths = []

for path in images.keys() :
    tmpImg = Image.new('RGB',(maxWidth,maxHeight),'white')
    offset = ( round((maxWidth - images[path].size[0])/2) , round((maxHeight - images[path].size[1])/2) )
    tmpImg.paste(images[path],offset)
    tmpPath = folderImages + "/" + "tmpgif" + path
    tmpPaths.append(tmpPath)
    tmpImg.save(tmpPath)
    #imagesResized.append(tmpImg)

nameOutput = char + "." + str(len(images))

subprocess.call(["convert" ,"-delay", "5","-loop","0", folderImages+"tmpgif"+"*" , nameOutput+".gif"])

subprocess.call(["rm" , folderImages + "tmpgif*"])

#writeGif(nameOutput,imagesResized,duration=1,dither=0)
