import operator
import os

import PySimpleGUI as sg

fileNames = []
fileExtensions = []
fileSizes = []
files = [fileNames], [fileExtensions], [fileSizes]

headings = ["File Name", "File Extension", "File Size (B)"]
folder_find_column = [
    [
        sg.Text("Enter Your Folder Adress"),
        sg.InputText(enable_events=True),
        sg.Button('Analyze', ),
        sg.Button("Browse Folder")
    ],
    [
        sg.Text("Total Number Of Files"),
        sg.Text(5, key= "-NumOfFiles-")
    ],
    [
        sg.Text("Total Size Of Folder (kB)"),
        sg.Text(700, key= "-TotalSize-")
    ],
    [
        sg.Button("Compress Folder")
    ],
    [
        sg.Button("Create File")
    ]
]
folder_viewer_column = [
    [
        sg.Button("Filter By File Extension"),
        sg.Button("Filter By File Size"),
        sg.Button("Sort By File Name"),
        sg.Button("Sort By File Extension"),
        sg.Button("Sort By File Size")
    ]
    ,
    [
        sg.Table(values=files, headings=headings, def_col_width=20, auto_size_columns=False, enable_events=True,
                 key="-FILE LIST-")
    ]

]

layout = [
    [
        sg.Column(folder_find_column),
        sg.VSeperator(),
        sg.Column(folder_viewer_column),
    ]
]

window = sg.Window('Image Viewer', layout)


def current_path():
    print("Current working directory before")
    print(os.getcwd())


def mkdir():
    directory = "Deneme"
    parent_dir = os.getcwd() + "/"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)


def listFiles(pather):
    path = pather + "/"
    dir_list = os.listdir(path)
    # print(dir_list)
    file_list = []
    size_list = []
    for i in dir_list:
        if '.' in i and i[0] != ".":
            file_list.append(i)
            size_list.append(fileSize(path + i))
    # print("Files in '", path, "' :")
    # print(file_list)
    filesWithSizes = [file_list],[size_list]
    return filesWithSizes


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
    # print(os.path.getsize(fn), "bytes")
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
            print(splitted[-1] + '.' + splitted[0])
            beforeRev.append(splitted[-1] + '.' + splitted[0])
        else:
            notDot.append(f)
    beforeRev = sorted(beforeRev)
    print(beforeRev)
    reversed = []
    for f in beforeRev:
        splitted = f.split('.')
        reversed.append(splitted[-1] + '.' + splitted[0])
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


while True:

    event, values = window.read()
    print(values[0])
    if event == 'Analyze':
        fileNames = listFiles(values[0])[0][0]
        fileExtensions = listFiles(values[0])[0][0]
        fileSizes = listFiles(values[0])[1][0]
        indexOfArray = 0
        sizeOfFolder = 0
        files = []
        print(fileNames)
        print(fileExtensions)
        print(fileSizes)

        while indexOfArray < len(fileNames):
            columnOne = fileNames[indexOfArray][fileNames[indexOfArray].index("."):]
            columnTwo = fileNames[indexOfArray][:fileNames[indexOfArray].index(".")]
            columnThree = fileSizes[indexOfArray]
            sizeOfFolder = (sizeOfFolder + columnThree)/1024
            newRow = [columnTwo, columnOne, columnThree]
            files.append(newRow)
            indexOfArray = indexOfArray + 1
        window.Element('-NumOfFiles-').Update(len(fileNames))
        window.Element('-TotalSize-').Update(sizeOfFolder)
        window.Element('-FILE LIST-').Update(values=files)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

# isFile("/Users/bartukaynar/PycharmProjects/FileManager/main.py")
# sortBySize(os.getcwd())
# sortByName(os.getcwd())
# sortBySize("/Users/bartukaynar/PycharmProjects/FileManager")
# sort_by_ext(os.getcwd())
