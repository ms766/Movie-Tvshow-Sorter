#!/usr/bin/env python3
from VideoRenamerVER2_Z import *;

#Empty list
done = []

#colors for text output
Red = "\u001b[31m";Green = "\u001b[32m";Yellow="\u001b[33m";Reset = "\u001b[0m";UNDERLINE = '\033[4m';LightCyan = '\033[96m';Magenta = "\033[35m";Blue = "\u001B[34m"; Turk = "\033[36m";lightgrey='\033[37m'; Blink = "\u001B[5m";

print(UNDERLINE+Magenta+"\t\t\t\t GENERAL SETTINGS                             \n"+Reset)

#Root path read in from file to where videos files are saved
try:
    rpathx = open('VideoFile-4.txt')
    rpathx = rpathx.read(); print(Blue+"Root D: "+Reset,rpathx)
except:
    print("file missing")

try:
    #path read in from file to where videos files are saved
    pathx = open('VideoFile-1.txt')
    pathx = pathx.read(); print(Turk+"CW Dir: "+Reset,pathx)
except:
    print("file missing")

try:
    #Good Extention list
    Ext = open('VideoFile-2.txt')
    Ext = Ext.read().split('\n');
    #removes empty strings from list
    Ext = list(filter(None, Ext));print(Green+"G Exts: "+Reset, Ext)
except:
    print("file missing")

try:
    #Junk Extention list
    JExt = open('VideoFile-3.txt')
    JExt = JExt.read().split('\n');
    #removes empty strings from list
    JExt = list(filter(None, JExt)); print(Red+"B Exts: "+Reset,JExt)
except:
    print("file missing")

try:
    AcronymList = open('ThreeLettercharsList.txt')
    AcronymList = AcronymList.read().split('\n');
    AcronymList = list(filter(None, AcronymList));print(lightgrey+"AcList: "+Reset, AcronymList)
except:
    print("file missing")





print(Magenta+UNDERLINE+"\t\t\t\t\t\t\t\t\t      ")

print("\n"+Red+"NOT satisfied:"+Reset+" with any of the settings above then "+Red+"Enter "+"'y'"+Reset+" for reset options ")
print(Green+"ARE Satisfied:"+Reset+" with all of the settings above then "+Green+"Enter "+"'n'"+Reset+" to continue !!!!!")
print(Yellow+"\nNote:"+Reset+" this prompt with will timeout in "+Red+"1"+Reset+" secounds"+Reset)

try:
    ResetOptionINPUT = inputimeout(Yellow+"Enter here: "+Reset,timeout = 1)
    if ResetOptionINPUT == "y":
        froot = open('VideoFile-4.txt')
        froot = froot.read()
        os.chdir(froot)
        os.system("clear && printf '\e[3J'")
        os.system("./VideoRenamerVER2_Y.py")


except TimeoutOccurred:
    print(UNDERLINE+Red+"\n\t\t\t\tSorry Times up\t\t\t\t\t"+Reset)
