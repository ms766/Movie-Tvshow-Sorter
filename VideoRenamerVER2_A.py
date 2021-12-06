#!/usr/bin/env python3
from VideoRenamerVER2_W import *;


def driver(path):
    if os.path.exists(path):
        os.chdir(path)
        for E in Ext:
            for J in JExt:
                junkremoval(path,E,J)
                rtvF(path,E)
                rmF(path,E)
        rtvFolder(path)
        mFolderRename(path)
        for E in Ext:
            moviefoldercreator(E,path)
        for E in Ext:
            season(path,E)
            Fcheck(path,E)
        for E in Ext:
            putbackListCreator(path,E)
        putback(path)

    if os.path.exists(pathx):
        os.chdir(pathx)
        finSorter(pathx)

    else:
        print('path error in terms of video files')

driver(pathx)
