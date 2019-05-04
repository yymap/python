#! python3
'''
Search file contents under a specific directory
'''

import os,re

def searchDir(fileOrDirName, searchKey):
    if not os.path.exists(fileOrDirName):
        print('Invalid file name or path:' + fileOrDirName)
        return
    
    if os.path.isfile(fileOrDirName):
        result = searchFileContent(fileOrDirName, searchKey)
        if result != None:
            print(result)
            return
    
    #fileOrDirNameAbsPath = os.path.abspath(fileOrDirName)
    
    resultList = []
    for folderName,subFolders,subFiles in os.walk(fileOrDirName):
        if subFiles == None:
            continue
        print('Current dir:' + folderName)
        for fileName in subFiles:
            if not fileName.endswith('.txt'):
                continue
            
            resultList += searchFileContent(os.path.join(folderName,fileName),searchKey)
    
    if resultList == None:
        print('No result.')
        return
    
    print('Result count:' + str(len(resultList)))
    print('\n'.join(resultList))
    

def searchFileContent(fileName,searchKey):    
    print('FileName:' + fileName)
    if not os.path.exists(fileName):
        print('File ' + fileName + ' Not exists.')
        return ''
    
    f = open(fileName)
    reg = re.compile(r'' + searchKey)
    listResult = []
    for lineContent in f.readlines():
        if reg.search(lineContent) != None:
            listResult.append(lineContent)
    f.close()
    return listResult


def testSearchDir():
    searchDir('..', 'EEE')
    
testSearchDir()
    
    
    