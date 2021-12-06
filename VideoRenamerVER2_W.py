#!/usr/bin/env python3
from VideoRenamerVER2_X import *;

#Global Var Notes
#Ext:  is a list of good f Extentions , JExt: is a like of bad f Extentions,
#Colors & etc txt formarting: Red , Green , Yellow , LightCyan , Magenta , Blue , Turk , lightgrey , Reset , UNDERLINE , Blink
#Lists: 1 done == empty
#path: pathX



ThreeLPcheck = os.path.isfile("ThreeLettercharsList.txt")
if ThreeLPcheck == False:
    f = open("ThreeLettercharsList.txt","w")
else:
    f = open("ThreeLettercharsList.txt","a")


ThreeLcINPUT = True; print()
try:
    print("\n"+Green+"Enter 'y'"+Reset+" to update Acronym List."+Green+"\nNote:"+Reset+" all 'acronyms' in a given string will be set to all caps"+Reset)
    print(Green+"Note:"+Reset+" this prompt with will timeout in "+LightCyan+"1"+Reset+" secounds"+Reset)
    Threein = inputimeout(Green+"Enter Here: "+Reset,timeout = 1)
    print()
    if Threein == 'y':
        while ThreeLcINPUT:
            ThreeinIN = input(Yellow+"Enter Acronym Here: "+Reset).title()
            if ThreeinIN == 'Done':
                ThreeLcINPUT = False
                f.close()
            else:

                f.write(ThreeinIN+'\n')
                print("Enter "+Red+"'done'"+Reset+" when you are finished entering acronyms\n")
    f.close()
    print()
except TimeoutOccurred:
    print(UNDERLINE+Red+"\n\t\t\t\tSorry Times up\t\t\t\t\t"+Reset)

def acronymListGen():
    f = open('ThreeLettercharsList.txt')
    genString = f.read().split('\n');
    genString = list(filter(None, genString));
    return genString
aList = acronymListGen()
print()


#<-----------------------------------------------------------------------

def junkremoval(path,Ext,jF):
    trashed=[]
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(jF) or 'sample' in filename.lower():
                try:
                    os.remove(filepath)
                except:
                    continue;

def emptyTV_EP_FolderRemoval(path):
    for root, dirs, files in os.walk(path):
         for item in dirs:
            if 'ENDLINE-Show' in item:
                os.rmdir(item)


# base pattern search which help sorts tv shows
def baseShow(baseString):
    namefix = baseString.lower().title()
    textRep = re.sub(r'[-[\]\._,#@%*()!^$\\]', ' ', namefix).lstrip().rstrip().replace("S0", "S").replace("E0"," E")#junk char removal & char replacement
    textRep = re.sub(r'\b([SE])(\d{1,2})', r'\1\2 ', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    textRep = re.sub(r'\b([E])(\d{1,2}) ', r'\1\2 ENDLINE-Show' ,textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    textRep = re.sub(r'(\b(\d){4}\b)','', textRep,flags=re.IGNORECASE) # if year in show title then delete
    return textRep

def endLineShow(textRep):
    textRep = re.sub(r' ENDLINE-Show.*$', '', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    textRep = re.sub(r'[ \s]{1,}', ' ', textRep,flags=re.IGNORECASE) # space greater than 1 char
    return textRep


def rtvF(path,Ext):
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(Ext):
                for name in filename.split(Ext):
                    if name == "":
                        pass
                    else:
                        textRep = baseShow(name)
                        if "ENDLINE-Show" in textRep:
                            textRep = endLineShow(textRep)
                            textRep = textRep+Ext
                            if textRep not in done:
                                fiRename = os.rename(filepath,textRep)
                                done.append(textRep)

def rtvFolder(path):
    for subdir, dirs, files in os.walk(path):
        for directoryitem in dirs:
            textRep = baseShow(directoryitem)
            if "ENDLINE-Show" in textRep:
                try:
                    fiRename = os.rename(directoryitem,textRep)
                    emptyTV_EP_FolderRemoval(path)
                except:
                    print('TVF renaming or removal error')


def season(path,Ext):
    for root, dirs, files in os.walk(path):
         for dir in dirs:
             if 'season' in dir.casefold():
                 namefix = dir.lower().title()
                 textRep = re.sub(r'[-[\]\._,#@%*()!^$\\]', ' ', namefix).lstrip().rstrip()
                 textRep = re.sub(r'[-]', ' - ', textRep) # -
                 textRep = re.sub(r'(\b(\d){4}\b)','', textRep,flags=re.IGNORECASE) # if year in show title then delete
                 textRep = re.sub(r'(season)\s?(\d{1,2})(.*)', r'\1 \2 ENDLINE-Show' ,textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
                 textRep = re.sub(r' ENDLINE-Show.*$', '', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
                 if textRep not in done:
                     fiRename = os.rename(dir,textRep)
                     done.append(textRep)
             else:
                 Seasonmatch = re.findall(r'\b(s\d{1,2})', dir,flags=re.IGNORECASE)
                 Seasonmatch = str(Seasonmatch)
                 S0somthing = Seasonmatch.lstrip("'[").rstrip("']")
                 Seasonmatch = re.sub(r's', 'Season ', S0somthing,flags=re.IGNORECASE)
                 namefix = dir.lower().title()
                 textRep = namefix.replace(S0somthing,Seasonmatch)
                 textRep = re.sub(r'[-[\]\._,#@%*()!^$\\]', ' ', textRep).lstrip().rstrip()
                 textRep = re.sub(r'[-]', ' - ', textRep) # -
                 textRep = re.sub(r'(\b(\d){4}\b)','', textRep,flags=re.IGNORECASE) # if year in show title then delete
                 textRep = re.sub(r'(season)\s?(\d{1,2})(.*)', r'\1 \2 ENDLINE-Show' ,textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
                 textRep = re.sub(r' ENDLINE-Show.*$', '', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
                 textRep = textRep.replace('Season 0','Season ')
                 if 'season' in textRep.casefold():
                     if textRep not in done:
                         fiRename = os.rename(dir,textRep)
                         done.append(textRep)


def baseMovie(baseString):
    namefix = baseString.lower().title()
    textRep = re.sub(r'[-[\]\._,#@%*()!^$\\]', ' ', namefix).lstrip().rstrip().replace("S0", "S").replace("E0"," E")#junk char removal & char replacement
    textRep = re.sub(r'\b([SE])(\d{1,2})', r'\1\2 ', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    textRep = re.sub(r'\b([E])(\d{1,2}) ', r'\1\2 ENDLINE-Show' ,textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    return textRep

def endlineMovie(textRep):
    textRep = re.sub(r'(\b(\d){4}\b)', r'[\1] ENDLINE', textRep,flags=re.IGNORECASE)
    textRep = re.sub(r' ENDLINE.*$', '', textRep, flags=re.IGNORECASE) #\1 refers to group 1 which is SE and \2 refers to group 2 which is \d
    textRep = re.sub(r'[\[]{2,}', '[', textRep,flags=re.IGNORECASE) # [ greater than 1 char
    textRep = re.sub(r'[\]]{2,}', ']', textRep,flags=re.IGNORECASE) # [ greater than 1 char
    textRep = re.sub(r'[ \s]{1,}', ' ', textRep,flags=re.IGNORECASE) # space greater than 1 char
    return textRep

def rmF(path,Ext):
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(Ext):
                if filename not in done:
                    for name in filename.split(Ext):
                        if name == "":
                            pass
                        else:
                            textRep = baseMovie(name)
                            movie_match = re.findall(r'(\b(\d){4}\b)', textRep,flags=re.IGNORECASE)
                            movie_matched = bool(movie_match)
                            if movie_matched == True:
                                textRep = endlineMovie(textRep)
                                textRep = textRep+Ext
                                if textRep not in done:
                                    fiRename = os.rename(filepath,textRep)
                                    done.append(textRep)



def mFolderRename(path):
    mp3dir=[]
    for root, dirs, files in os.walk(path):
         for item in dirs:
             match = re.findall(r'(\b(\d){4}\b)', item,flags=re.IGNORECASE)
             matched = bool(match)
             if matched == True:
                 os.chdir(path+"/"+item)
                 cwdITEMSlist = os.listdir(os.getcwd())
                 for fileINd in cwdITEMSlist:
                     if fileINd.endswith('.mp3'):
                         cwd = os.getcwd()
                         if cwd not in mp3dir:
                             mp3dir.append(cwd)
    os.chdir(path)
    for subdir, dirs, files in os.walk(path):
        for directoryitem in dirs:
            textRep = baseMovie(directoryitem)
            movie_match = re.findall(r'(\b(\d){4}\b)', textRep,flags=re.IGNORECASE)
            movie_matched = bool(movie_match)
            if movie_matched == True:
                textRep = endlineMovie(textRep)
                for m in mp3dir:
                    if m != path+"/"+directoryitem and path+"/"+directoryitem not in mp3dir:
                        if textRep not in done:
                            fiRename = os.rename(directoryitem,textRep)
                            done.append(textRep)
                if len(mp3dir) == 0:
                    fiRename = os.rename(directoryitem,textRep)

def moviefoldercreator(Ext, path):
    os.chdir(path)
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(Ext):
                movie_match = re.findall(r'(\b(\d){4}\b)', filename,flags=re.IGNORECASE)
                movie_matched = bool(movie_match)
                if movie_matched == True:
                    filenameNoEXt = filename.strip(Ext)
                    if os.path.isdir(filenameNoEXt) == False:
                        try:
                            os.makedirs(filenameNoEXt)
                        except:
                            continue;

def forecRename():
    os.chdir(pathx)
    for word in aList:
        titleW = word.title()
        caps = word.upper()
        try:
            os.system("rename -f 's/{}/{}/' *".format(titleW,caps))
            for E in Ext:
                os.system("rename -f 's/{}/{}/' {}".format(titleW,caps,E))
        except:
            pass

#for renames files with acronyms in there names
def Fcheck(path,Ext):
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(Ext):
                for name in filename.split(Ext):
                    if name == "":
                        pass
                    else:
                        for word in aList:
                            word = word.lower()
                            filename = filename.lower()
                            if word in filename:
                                forecRename()

dirlist = []; fileslist = [];
def putbackListCreator(path,Ext):
    os.chdir(path)
    for root, dirs, files in os.walk(path):
            for dir in dirs:
                if dir in dirlist:
                    pass;
                else:
                    dirlist.append(dir)
            for file in files:
                if file.endswith(Ext):
                    fileslist.append(file);


def putback(path):
    for i in range(len(fileslist)):
        for ditem in dirlist:
            for fitem in fileslist:
                fseasonNum = re.findall(r'S\d{1,2}', fitem)
                fseasonNum = str(fseasonNum)
                fseasonNum = fseasonNum.lstrip("'[").rstrip("']")

                ditemx = ditem.replace('Season ', 'S')

                dseasonNum = re.findall(r'S\d{1,2}', ditemx)
                dseasonNum = str(dseasonNum)
                dseasonNum = dseasonNum.lstrip("'[").rstrip("']")


                #movie check
                rootMitem = re.sub(r'[.][a-z0-9]+','', fitem,flags=re.IGNORECASE)
                if rootMitem == ditem:
                    try:
                        shutil.move(path+"/"+fitem,path+"/"+ditem)
                    except:
                        continue;

                #season check
                rootFitemShow = re.sub(r'S\d{1,2} E\d{1,2}[.][a-z]+','', fitem,flags=re.IGNORECASE)
                rootDitemShow = re.sub(r'Season.*','', ditem,flags=re.IGNORECASE)
                if rootFitemShow == rootDitemShow and fseasonNum == dseasonNum:
                    try:
                        shutil.move(path+"/"+fitem,path+"/"+ditem)
                    except:
                        continue;

#<---------------------

def finSorter(path):
    for root, dirs, files in os.walk(path):
         for item in dirs:
             match = re.findall(r'\b(season+\s\d{1,2})\b', item,flags=re.IGNORECASE)
             matched = bool(match)
             if matched == True:
                 try:
                     shutil.move(path+"/"+item,'/Users/ms/Desktop/0 DoWnLoAdS/1-TV Shows')
                 except:
                     continue;
    for root, dirs, files in os.walk(path):
         for item in files:
            match = re.findall(r'\b([SE])(\d{1,2})', item,flags=re.IGNORECASE)
            matched = bool(match)
            if matched == True:
                try:
                    shutil.move(path+"/"+item,'/Users/ms/Desktop/0 DoWnLoAdS/1-TV Shows')
                except:
                    continue;
    mp3dir=[]; musicSwitch = False;
    for root, dirs, files in os.walk(path):
         for item in dirs:
             match = re.findall(r'(\b(\d){4}\b)', item,flags=re.IGNORECASE)
             matched = bool(match)
             if matched == True:
                 os.chdir(path+"/"+item)
                 cwdITEMSlist = os.listdir(os.getcwd())
                 for fileINd in cwdITEMSlist:
                     if fileINd.endswith('.mp3'):
                         musicSwitch = True;
                         cwd = os.getcwd()
                         if cwd not in mp3dir:
                             mp3dir.append(cwd)
    os.chdir(path)


    for root, dirs, files in os.walk(path):
         for item in dirs:
             match = re.findall(r'(\b(\d){4}\b)', item,flags=re.IGNORECASE)
             matched = bool(match)
             if matched == True and musicSwitch == False:
                 try:
                     shutil.move(path+"/"+item,'/Users/ms/Desktop/0 DoWnLoAdS/0-movie')
                 except:
                    continue;
             if matched == True and musicSwitch == True:
                 for m in mp3dir:
                    if m != path+"/"+item and path+"/"+item not in mp3dir:
                        try:
                            shutil.move(path+"/"+item,'/Users/ms/Desktop/0 DoWnLoAdS/0-movie')
                        except:
                            continue;
                    if len(mp3dir) == 0:
                        try:
                            shutil.move(path+"/"+item,'/Users/ms/Desktop/0 DoWnLoAdS/0-movie')
                        except:
                           continue;
