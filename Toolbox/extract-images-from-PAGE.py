#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
from PIL import Image
from xml.dom import minidom
folderInputXMLs = sys.argv[1]
folderInputImgs = sys.argv[2]
folderOutputPath = sys.argv[3]

#check name and create outputFolder
if folderOutputPath[-1]!="/":
    folderOutputPath+="/"
subprocess.call(["mkdir","-p",folderOutputPath])

gobalGlyphCount=0
#inputs unsorted
inputXMLs=os.listdir(folderInputXMLs)
inputImgs=os.listdir(folderInputImgs)
#inputs sorted and matched
XMLs={}
Imgs={}
# check if the number of PAGE files and page image match.
if len(inputXMLs)==len(inputImgs):
    for f in inputXMLs:
        # get page number and match it with it XMLPAGE file parsed in a dictionnary : XMLs[page] = page.xml
        pageXML = re.findall('\d+', f)[0]
        XMLs[pageXML] = minidom.parse(folderInputXMLs+f)
    for i in inputImgs:
        # get page number and match it with it .png file parsed by PIL in a dictionnary : Imgs[page] = page.png
        pageImg = re.findall('\d+', i)[0]
        Imgs[pageImg]= Image.open(folderInputImgs+"/"+i)

    for pageNumber, xmlPage in XMLs.items(): # page by page

        imgPage = Imgs[pageNumber]

        root = xmlPage.documentElement
        # xml browsing
        nodeGlyphs = root.getElementsByTagName('Glyph')

        BarByPage = ProgressBar(len(nodeGlyphs), 30 , 'Extraction page '+pageNumber)

        unicodeChars = []
        coordsCorpList = []
        for n in nodeGlyphs : # glyph by glyph
            # get glyph's name (char)
            char = n.getElementsByTagName('Unicode')[0].firstChild.nodeValue
            unicodeChars.append(char)
            # get glyph's coords (and parse from xml)
            coords = n.getElementsByTagName('Coords')[0].getAttribute('points')
            coords = coords.split(' ')
            coordCrop = [coords[0].split(','),coords[2].split(',')]
            for c in coordCrop:
                c[0]=int(c[0])
                c[1]=int(c[1])
            # margining
            coordCrop[0][0]-=2;
            coordCrop[0][1]-=2;
            coordCrop[1][0]+=2;
            coordCrop[1][1]+=2;
            # crop the image of in the glyph in the image of the page
            area = imgPage.crop((coordCrop[0][0],coordCrop[0][1],coordCrop[1][0],coordCrop[1][1]))
            area.save(folderOutputPath+char+pageNumber+"-"+str(gobalGlyphCount)+".png")
            gobalGlyphCount+=1

            BarByPage.update()
            #coordsCorpList.append(coordCrop)

else:
    print("PAGE files and page image don't match")
