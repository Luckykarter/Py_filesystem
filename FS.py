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
            try:
                listAll(cpath, onlydirs, maxlevel, level + 1)
            except:
                print("\n" + cpath + " not accessible")
        elif not onlydirs:
            printL(cpath, level)

if __name__ == '__main__':
    dir = input("Enter directory: \n")
    if not os.path.isdir(dir):
        print(dir + " is not a valid directory")
        exit(1)
    only = input("Only directories? (y/n)\n").lower()
    maxlevel = int(input("Maximum level of sub-directories\n"))

    listAll(dir, onlydirs=(only[0]=="y"), maxlevel=maxlevel)


