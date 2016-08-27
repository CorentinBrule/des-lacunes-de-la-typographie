#!/usr/bin/python3.4
# coding: utf8

import sys,os,subprocess

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
    print(d,f)

folders2averages=sys.argv[1:]

for f in folders2averages:
        images=listdir_fullpath(f)
        subprocess.call(["convert"]+images+["-average",f+"average.png"])
