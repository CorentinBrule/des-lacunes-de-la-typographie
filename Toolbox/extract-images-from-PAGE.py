#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re

from PIL import Image
from xml.dom import minidom
folderInputXMLs = sys.argv[1]
folderInputImgs = sys.argv[2]
folderOutputPath = sys.argv[3]
subprocess.call(["mkdir","-p",folderOutputPath])

j=0

inputXMLs={}
inputImgs={}
if len(os.listdir(folderInputXMLs))==len(os.listdir(folderInputImgs)):
    for f in os.listdir(folderInputXMLs):
        pageXML = re.findall('\d+', f)[0]
        inputXMLs[pageXML] = minidom.parse(folderInputXMLs+f)
    for i in os.listdir(folderInputImgs):
        pageImg = re.findall('\d+', i)[0]
        inputImgs[pageImg]= Image.open(folderInputImgs+"/"+i)

    for nb, xmlPage in inputXMLs.items():

        imgPage = inputImgs[nb]


        root = xmlPage.documentElement

        nodeGlyphs = root.getElementsByTagName('Glyph')

        unicodeChars = []
        coordsCorpList = []
        for n in nodeGlyphs :

            char = n.getElementsByTagName('Unicode')[0].firstChild.nodeValue
            unicodeChars.append(char)

            coords = n.getElementsByTagName('Coords')[0].getAttribute('points')
            coords = coords.split(' ')
            coordCrop = [coords[0].split(','),coords[2].split(',')]
            for c in coordCrop:
                c[0]=int(c[0])
                c[1]=int(c[1])

            area = imgPage.crop((coordCrop[0][0],coordCrop[0][1],coordCrop[1][0],coordCrop[1][1]))
            area.save(folderOutputPath+char+nb+"-"+str(j)+".png")
            j+=1
            #area = imgPage.crop(())

            coordsCorpList.append(coordCrop)
