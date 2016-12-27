#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *

letter = sys.argv[1]
levels = sys.argv[2:]
resize = "300%" #define rescale factor
delta = 10 #define delta of the levels : the contrast factor
char = letter.split("/")[-1][0] #get the name of the glyph

progressBar = ProgressBar(len(levels), 30 , "Niveaux : ")

subprocess.call(["convert",letter,"-resize",resize,char+".png"]) #save a rescale version
#save rescale and modify versions
for level in levels:
    print(level)
    m = int(level)-delta/2
    M = int(level)+delta/2
    parameter = str(m)+"%,"+str(M)+"%" #ex : 45%,55% with level=50% and delta=10%
    output = char+level+"pc"+str(delta)+"d.png"
    subprocess.call(["convert",letter,"-resize",resize,"-level",parameter,output])

    progressBar.update()
