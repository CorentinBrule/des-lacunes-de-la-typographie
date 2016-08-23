#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re

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

inputXMLs={}
inputImgs={}
# check if the number of PAGE files and page image match.
if len(os.listdir(folderInputXMLs))==len(os.listdir(folderInputImgs)):
    for f in os.listdir(folderInputXMLs):
        # get page number and match it with it XMLPAGE file parsed in a dictionnary : inputXMLs[page] = page.xml
        pageXML = re.findall('\d+', f)[0]
        inputXMLs[pageXML] = minidom.parse(folderInputXMLs+f)
    for i in os.listdir(folderInputImgs):
        # get page number and match it with it .png file parsed by PIL in a dictionnary : inputXMLs[page] = page.png
        pageImg = re.findall('\d+', i)[0]
        inputImgs[pageImg]= Image.open(folderInputImgs+"/"+i)

    for pageNumber, xmlPage in inputXMLs.items(): # page by page

        imgPage = inputImgs[pageNumber]

        root = xmlPage.documentElement
        # xml browsing
        nodeGlyphs = root.getElementsByTagName('Glyph')

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

            #coordsCorpList.append(coordCrop)
else:
    print("PAGE files and page image don't match")
