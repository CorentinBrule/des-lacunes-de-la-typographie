#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess,re
from ProgressBar import *

resize = "300%"
letter = sys.argv[1]
levels = sys.argv[2:]
delta = 10
print(letter)
char = letter.split("/")[-1][0]

subprocess.call(["convert",letter,"-resize",resize,char+".png"])

for level in levels:
    print(level)
    m = int(level)-delta/2
    M = int(level)+delta/2
    parameter = str(m)+"%,"+str(M)+"%"
    output = char+level+"pc"+str(delta)+"d.png"
    subprocess.call(["convert",letter,"-resize",resize,"-level",parameter,output])
