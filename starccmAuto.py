# test
# Starccm Batch Automation Script with PB
# Need to install Python 3, Expect module

import sys
import os
import glob
import time
import subprocess

# Parameters
    starccmcommand = "starccm"
    defuserpswd = "ChangeToYOURS"
    pushbullettoken = "ChangeToYOURS"
    numofcores = "4"
    macrofile = "meshandrun.java"  # empty string "" if no macrofile is needed

# function to make files executable


def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2
    os.chmod(path, mode)


# user password can be passed as argument (or default)
if len(sys.argv) > 1:
    userpswd = sys.argv[1]
else:
    userpswd = defuserpswd

# current directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# check files are in place
if macrofile != "":
    macrodir = dir_path + "/" + macrofile
    if os.path.isfile(macrodir) == False:
        print("Error: Specified macro file not found in directory")
        sys.exit()
    macrodir = macrodir + " "
else:
    macrodir = ""

# list of .sim files
simfulldir = []
simfiles = glob.glob('*.sim')
numofsim = len(simfiles)
for simfile in simfiles:
    simfulldir.append(dir_path + '/' + simfile)
if simfiles == []:
    print("Error: No sim files found")
    sys.exit()

# expect script
with open('expectscript.exp', 'w') as f:
    f.write(r'#!/usr/bin/expect' + "\nset timeout -1\nspawn ./batch.sh")
    for i in range(numofsim):
        f.write("\n" + r'expect "password:" {send "' + userpswd + r'\r"}')
    f.write("\ninteract")

# bash script
with open('batch.sh', 'w') as f:
    f.write(r'#!/bin/bash' + "\n")
    for i, sim in enumerate(simfulldir):
        f.write(starccmcommand + " -batch -power -np " + numofcores +
                " " + macrodir + sim + " -podkey lM66SSsU2JDB0BfHbD8gFA" + "\n")
        f.write("curl -u " + pushbullettoken +
                ": https://api.pushbullet.com/v2/pushes -d type=note -d title=\"" + simfiles[i] + " finished\"\n")

# makes batch and expect script executable
make_executable(dir_path + r'/batch.sh')
make_executable(dir_path + r'/expectscript.exp')

# run simulations expect--> bash --> starccm
time.sleep(3)
subprocess.call(r'./expectscript.exp', shell=True)
