import os
import operator
from typing import List

def current_path():
    print("Current working directory before")
    print(os.getcwd())


def mkdir():
    directory = "Deneme"
    parent_dir = os.getcwd()+"/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)


def listFiles(pather):
    path = pather+"/"
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)
    return dir_list


def renameFile(fd, nd):
    os.rename(fd, nd)


def removeFolder(fn):
    os.rmdir(fn)


def removeFile(fn):
    os.remove(fn)


def findFile(name, path):
    exist = False
    for root, dirs, files in os.walk(path):
        if name in files:
            print(name, "exist in", root)
            exist = True
            return os.path.join(root, name)
    if exist == False:
        print("File does not exist in specified path.")


def findInAll(name):
    exist = False
    for root, dirs, files in os.walk("/"):
        if name in files:
            print(name, "exist in", root)
            exist = True
            return os.path.join(root, name)
    if exist == False:
        print("File does not exist.")


def fileSize(fn):
    print(os.path.getsize(fn), "bytes")
    return os.path.getsize(fn)


def folderSize(fn):
    size = 0
    for path, dirs, files in os.walk(fn):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    print("Folder size: " + str(size), "bytes")
    return size


def numberOfFiles(fn):
    print(len([name for name in os.listdir(fn)]))


def sortByName(fp):
    print(sorted(os.listdir(fp)))
    return sorted(os.listdir(fp))


def sortBySize(fp):
    files = os.listdir(fp)
    print(files)
    fileArray = {}
    for f in files:
        if isFile(f):
            fileArray[f] = fileSize(f)
        else:
            fileArray[f] = folderSize(f)
    sorted_d = sorted(fileArray.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_d)


def sort_by_ext(fn):
    files = sortByName(fn)
    beforeRev = []
    notDot = []
    for f in files:
        if '.' in f:
            splitted = f.split('.')
            print(splitted[-1]+'.'+splitted[0])
            beforeRev.append(splitted[-1]+'.'+splitted[0])
        else:
            notDot.append(f)
    beforeRev = sorted(beforeRev)
    print(beforeRev)
    reversed = []
    for f in beforeRev:
        splitted = f.split('.')
        reversed.append(splitted[-1]+'.'+splitted[0])
    for f in notDot:
        reversed.append(f)
    print(reversed)
    return reversed


def sortByExtension(fn):
    y = [f for f in os.listdir(fn)
         if os.path.isfile(os.path.join(fn, f))]
    print(y)
    y.sort(key=lambda f: os.path.splitext(f))
    print(y)

def isFile(fn):
    file_exists = os.path.isfile(fn)
    return file_exists


#isFile("/Users/bartukaynar/PycharmProjects/FileManager/main.py")
#sortBySize(os.getcwd())
#sortByName(os.getcwd())
#sortBySize("/Users/bartukaynar/PycharmProjects/FileManager")
#sort_by_ext(os.getcwd())