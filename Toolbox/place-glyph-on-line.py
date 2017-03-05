#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *
from PIL import Image
from xml.dom import minidom

folderInputXMLs = sys.argv[1]
folderInputImgGlyphs = sys.argv[2]
folderOutputPath = sys.argv[3]
