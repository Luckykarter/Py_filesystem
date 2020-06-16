import os
import shutil

def printL(p, level):
    t = str()
    for _ in range(0, level):
        t += "\t"
    print(t + p)

def listAll(path, onlydirs = False, maxlevel = None, level=0):

    printL(path, level)
    for p in os.listdir(path):
        cpath = os.path.join(path, p)
        if os.path.isdir(cpath):
            if maxlevel is not None:
                if maxlevel <= level:
                    return

            listAll(cpath, onlydirs, maxlevel, level + 1)
        elif not onlydirs:
            printL(cpath, level)

listAll("/Users/egorwexler", maxlevel=1)
