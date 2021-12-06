#!/usr/bin/env python3
from VideoRenamerVER2_Z import *;

#1 color varibles
Red = "\u001b[31m";Green = "\u001b[32m";Yellow="\u001b[33m";Reset = "\u001b[0m";UNDERLINE = '\033[4m';LightCyan = '\033[96m';Magenta = "\033[35m"

#2 check if path exists and reads in and out user input in regards to setting a file path for video files to be worked on
def pathcheck():
    pcheck = True
    vFPathChecker = os.path.isfile("VideoFile-1.txt")

    if vFPathChecker == False:
        vFPathINPUT = input("Enter a vaild directoy with 'tvshows' & 'movies' files to work on. \n"+Yellow+"For Exmaple: /home/self/Downloads <-> ON MAC or LINUX: "+Reset);print()

        f = open("VideoFile-1.txt", "w")
        f.write(vFPathINPUT)
        f.close()

        f = open("VideoFile-1.txt")
        read = f.read()
        f.close()

        isdir = os.path.isdir(read)
        if isdir == True:
            print(Green+"The current working directory has been UPDATED and is:"+Reset,os.getcwd());print()
            return()
        if isdir == False:
            pcheck = False
            if pcheck == False:
                os.system("rm VideoFile-1.txt")
                pathcheck()
    elif vFPathChecker == True:

            f = open("VideoFile-1.txt")
            read = f.read()
            f.close()

            isdir = os.path.isdir(read)
            if isdir == True:
                print(Green+"The current working directory is:"+Reset,os.getcwd());print()
                return()
            if isdir == False:
                pcheck = False
                if pcheck == False:
                    os.system("rm VideoFile-1.txt")
                    pathcheck()
pathcheck()

#3 Reads in and out text in the form of file extentions for the types of files that you would like to work on
def goodFileExts():
    gfExtList = []
    gFileExtschecker = os.path.isfile("VideoFile-2.txt")
    if gFileExtschecker == False:
        fE_INPUT = True
        while fE_INPUT:
            FileExtsINPUT = input("Enter file extentions for the types of files that you would like to work on. \n"+Yellow+"For Example: '.avi','.mkv','.mov', etc: "+Reset)
            if FileExtsINPUT != 'done' and FileExtsINPUT.startswith("."):
                gfExtList.append(FileExtsINPUT)
                print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset)

                f = open("VideoFile-2.txt", "a")
                f.write(FileExtsINPUT+"\n")
                f.close()

            else:
                os.system("clear && printf '\e[3J'")
            if FileExtsINPUT == 'done':
                fE_INPUT = False
                os.system("clear && printf '\e[3J'")
                print(Green+"The file Extentions you have chosen to work on have been updated and are"+Reset,gfExtList);print()
    else:
        f = open("VideoFile-2.txt")
        read = f.readlines()
        f.close()

        for item in read:
            if item != " ":
                gfExtList.append(item.rstrip('\n'))
        print("\n"+Green+"The file extentions stored and currently being worked on are: "+Reset,gfExtList);print("\n")
goodFileExts()

#4 Reads in and out text in the form of file extentions for the types of files that you would NOT like to work on
def junkfileExt():
    jfExtList = []
    junkFileExtschecker = os.path.isfile("VideoFile-3.txt")
    if junkFileExtschecker == False:
        JFEIN = True
        while JFEIN:
            junkFileExtsINPUT = input("Enter a JUNK file extentions for the types of files that you would "+Red+"NOT"+Reset+" like to work on. \n"+Yellow+"For Example: '.txt','.jpg','.NFO', etc: "+Reset)
            if junkFileExtsINPUT != 'done' and junkFileExtsINPUT.startswith("."):
                jfExtList.append(junkFileExtsINPUT)
                print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset)

                f = open("VideoFile-3.txt", "a")
                f.write(junkFileExtsINPUT+"\n")
                f.close()
            else:
                os.system("clear && printf '\e[3J'")
            if junkFileExtsINPUT == 'done':
                JFEIN = False
                os.system("clear && printf '\e[3J'")
                print("\n"+Green+"The JUNK file Extentions you have chosen "+Red+"NOT"+Green+" to work on has been updated and are"+Reset,jfExtList);print()
    else:
        f = open("VideoFile-3.txt")
        read = f.readlines()
        f.close()
        for item in read:
            if item != " ":
                jfExtList.append(item.rstrip('\n'))
        print(Green+"The JUNK file extentions stored and currently "+Red+"NOT"+Green+" being worked on are:"+Reset,jfExtList);print("\n")
junkfileExt()

# Asks user to set the root dir of where this file is saved
def rootScriptdir():
    jumpPointOne = True
    while jumpPointOne:
        #rootSpathINPUT = input("Enter the root directory where you stored this script to restart script. \n"+Red+"NOTE: Once this is done once you will not need to set the path for this file agian !!!"+Reset+"\n\n"+Green+"Enter Path here:"+Reset)

        f = open("VideoFile-4.txt", "w")
        f.write(os.getcwd())
        f.close()

        isdir = os.path.isdir(read)
        if isdir == True:
            jumpPointOne = False
            os.system("./VideoRenamerVER2_Y.py")
        else:
            os.system("clear && printf '\e[3J'")

rootPathChecker = os.path.isfile("VideoFile-4.txt")
if rootPathChecker == False:
    rootScriptdir()

rootPathChecker = os.path.isfile("VideoFile-4.txt")
if rootPathChecker == True:
    f = open("VideoFile-4.txt")
    read = f.read()
    if read == os.getcwd():
        f.close()
        print(Green+"The "+Red+"root"+Green+" directory where this file is saved is:"+Reset,read);print()
    else:
        os.system("rm VideoFile-4.txt")
        os.system("clear && printf '\e[3J'")
        rootScriptdir()

def starterCheckReset():
    fullResetINPUT = True
    while fullResetINPUT:
        os.system("clear && printf '\e[3J'")
        print(Red+"Note: "+Reset+UNDERLINE+"This prompt will"+Reset+" "+Reset+Red+"timeout"+Reset+" "+Reset+UNDERLINE+"in 2 seconds"+Reset+"\n")
        try:
            fullResetINPUT = inputimeout("If you made a mistake and would like to reset the"+Yellow+" Current working directoy"+Reset+","+Yellow+" file extentions to be work on"+Reset+","+Yellow+" JUNK file extentions "+Red+"NOT "+Yellow+"to be work on "+Reset+"and"+Yellow+" root directoy where this script is stored"+Reset+" then Enter"+Green+" y "+Reset+"otherwise Enter"+Red+" n "+Reset+": ", timeout=2)
            if fullResetINPUT == "y":
                fullResetINPUT = False
                os.system("rm VideoFile-1.txt")
                os.system("rm VideoFile-2.txt")
                os.system("rm VideoFile-3.txt")
                os.system("rm VideoFile-4.txt")
                os.system("clear && printf '\e[3J'")

                jumpPointOne = True

                while jumpPointOne:
                    rootPathChecker = os.path.isfile("VideoFile-4.txt")
                    if rootPathChecker == True:

                        isdir = os.path.isdir(read)
                        if isdir == True:
                            jumpPointOne = False
                            os.system("./VideoRenamerVER2_Y.py")
                        else:
                            jumpPointOne = False
                            os.system("clear && printf '\e[3J'")
                            os.system("./VideoRenamerVER2_Y.py")
                    else:
                        rootScriptdir()

            elif fullResetINPUT == "n":
                return
        except TimeoutOccurred:
            return

os.system("sleep 1")
starterCheckReset()



def starterCheckUpdate():
    os.system("clear && printf '\e[3J'")
    print(LightCyan+"Note: "+Reset+UNDERLINE+"This prompt will"+Reset+" "+Reset+LightCyan+"timeout"+Reset+" "+Reset+UNDERLINE+"in 2 seconds"+Reset+"\n")
    try:
        fullResetINPUT = inputimeout("If you made a mistake and would like to "+Red+"UPDATE"+Reset+" the"+Magenta+" Current working directoy"+Reset+","+Magenta+" file extentions to be work on"+Reset+" and"+Magenta+" JUNK file extentions "+Red+"NOT "+Magenta+"to be work on"+Reset+" then Enter"+Green+" y "+Reset+"otherwise Enter"+Red+" n "+Reset+": ", timeout=2)
        if fullResetINPUT == "y":
            os.system("clear && printf '\e[3J'")
            print("Enter "+Red+'1'+Reset+" to update Current working directoy\nEnter "+Red+'2'+Reset+" to update file extentions to be work\nEnter "+Red+'3'+Reset+" to update JUNK file extentions to be work\nEnter "+Red+'4'+Reset+" to update the root directoy path of where this script is saved\n")
            updatePrompt = input(Yellow+"Enter what you would like to UPDATE here: "+Reset)

            if updatePrompt == "1":
                os.system("clear && printf '\e[3J'")
                os.system("rm VideoFile-1.txt")
                os.system("./VideoRenamerVER2_Y.py")
            elif updatePrompt == "2":#<----------------------
                os.system("clear && printf '\e[3J'")
                goodFileExts()
                print("Would you like to "+Green+"add"+Reset+" an item to the list above or "+Red+"del"+Reset+" one?\n")
                print("Enter "+Green+"1 "+Reset+"to "+Green+"add"+Reset+"\nEnter "+Red+"2 "+Reset+"to "+Red+"del \n"+Reset)
                addORdelINPUT = input(Yellow+"Enter what you would like to do here: "+Reset)
                if addORdelINPUT == "1":
                    fE_INPUT = True
                    while fE_INPUT:
                        print();
                        FileExtsINPUT = input("Enter file extentions for the types of files that you would like to "+Red+"ADD "+Reset+"to the list above. \n"+Yellow+"For Example: '.avi','.mkv','.mov', etc: "+Reset)
                        if FileExtsINPUT != 'done' and FileExtsINPUT.startswith("."):
                            print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset);

                            f = open("VideoFile-2.txt", "a")
                            f.write(FileExtsINPUT+"\n")
                            f.close()

                        if FileExtsINPUT == "done":
                            fE_INPUT = False
                            os.system("clear && printf '\e[3J'")
                            goodFileExts()
                            os.system("sleep 1")
                            os.system("./VideoRenamerVER2_Y.py")
                elif addORdelINPUT == "2":

                    fE_INPUT = True
                    while fE_INPUT:
                        print();
                        FileExtsINPUT = input("Enter file extentions for the types of files that you would like to "+Red+"DELETE "+Reset+". \n"+Yellow+"For Example: '.avi','.mkv','.mov', etc: "+Reset)
                        if FileExtsINPUT != 'done' and FileExtsINPUT.startswith("."):
                            print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset);

                            f = open("VideoFile-2.txt",'r+')
                            read = f.read()
                            text = re.sub(FileExtsINPUT, '', read)
                            text = text.split('\n')

                            estring=""
                            for ext in text:
                                if ext != "":
                                    ext = ext.strip()
                                    estring += ext+'\n'
                            f.seek(0)
                            f.write(estring)
                            f.truncate()
                            f.close()

                        if FileExtsINPUT == "done":
                            fE_INPUT = False
                            os.system("clear && printf '\e[3J'")
                            goodFileExts()
                            os.system("sleep 1")
                            os.system("./VideoRenamerVER2_Y.py")
                else:
                    return
            elif updatePrompt == "3":
                os.system("clear && printf '\e[3J'")
                junkfileExt()
                print("Would you like to "+Green+"add"+Reset+" an item to the list above or "+Red+"del"+Reset+" one?\n")
                print("Enter "+Green+"1 "+Reset+"to "+Green+"add"+Reset+"\nEnter "+Red+"2 "+Reset+"to "+Red+"del \n"+Reset)
                addORdelINPUT = input(Yellow+"Enter what you would like to do here: "+Reset)
                if addORdelINPUT == "1":
                    fE_INPUT = True
                    while fE_INPUT:
                        print();
                        FileExtsINPUT = input("Enter JUNK file extentions for the types of files that you would like to "+Red+"ADD "+Reset+"to the list above. \n"+Yellow+"For Example: '.avi','.mkv','.mov', etc: "+Reset)
                        if FileExtsINPUT != 'done' and FileExtsINPUT.startswith("."):
                            print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset);

                            f = open("VideoFile-3.txt", "a")
                            f.write(FileExtsINPUT+"\n")
                            f.close()

                        if FileExtsINPUT == "done":
                            fE_INPUT = False
                            os.system("clear && printf '\e[3J'")
                            junkfileExt()
                            os.system("sleep 1")
                            os.system("./VideoRenamerVER2_Y.py")
                elif addORdelINPUT == "2":

                    fE_INPUT = True
                    while fE_INPUT:
                        print();
                        FileExtsINPUT = input("Enter JUNK file extentions for the types of files that you would like to "+Red+"DELETE "+Reset+". \n"+Yellow+"For Example: '.avi','.mkv','.mov', etc: "+Reset)
                        if FileExtsINPUT != 'done' and FileExtsINPUT.startswith("."):
                            print(Red+"Enter 'done' when you are finished entering file extention types\n"+Reset);

                            f = open("VideoFile-3.txt",'r+')
                            read = f.read()
                            text = re.sub(FileExtsINPUT, '', read)
                            text = text.split('\n')

                            estring=""
                            for ext in text:
                                if ext != "":
                                    ext = ext.strip()
                                    estring += ext+'\n'
                            f.seek(0)
                            f.write(estring)
                            f.truncate()
                            f.close()

                        if FileExtsINPUT == "done":
                            fE_INPUT = False
                            os.system("clear && printf '\e[3J'")
                            junkfileExt()
                            os.system("sleep 1")
                            os.system("./VideoRenamerVER2_Y.py")

            elif updatePrompt == "4":
                os.system("clear && printf '\e[3J'")
                rootScriptdir()
            else:
                return

    except TimeoutOccurred:
        return
starterCheckUpdate()
