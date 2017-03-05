#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
from PIL import Image
from xml.dom import minidom

import extract

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

        #unicodeChars = []
        coordsCorpList = []
        for n in nodeGlyphs : # glyph by glyph

            area,outputName = extract.extract(n)
            area.save(folderOutputPath + outputName)
            BarByPage.update()
            #coordsCorpList.append(coordCrop)

else:
    print("PAGE files and page image don't match")
