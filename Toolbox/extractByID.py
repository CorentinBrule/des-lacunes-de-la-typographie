#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
from PIL import Image
from xml.dom import minidom

import extract

fileInputXML = sys.argv[1]
fileInputImg = sys.argv[2]
nodeIds = sys.argv[3:]

xml = minidom.parse(fileInputXML)
imgPage = Image.open(fileInputImg)
#nodes = xml.getElementsByTagName("Glyph")

#node = xml.getElementsByTagName("Glyph")[0]
for i in nodeIds:

    node = extract.findElementById(xml,i)
    area,outputName = extract.extract(imgPage,node)
    area.save(outputName)
