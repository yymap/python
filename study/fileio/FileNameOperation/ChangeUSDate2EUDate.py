#! python3
'''
If there are many files is named with US date format, and you want to change the 
file name to EU date format, you can use this function.
US Date format: MM-DD-YYYY
EU Date format: DD-MM-YYYY
'''

import os,shutil,re


def renameDirFiles(dirPath):
    if not os.path.isdir(dirPath):
        return 'Not directory name.'
    if not os.path.exists(dirPath):
        return 'Directory ' + dirPath + ' not exists.'
    dirFiles = os.listdir(dirPath)
    if len(dirFiles) == 0:
        return 'Empty directory.'
    
    reg = re.compile(r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$')
    
    for fileName in dirFiles:
        ret = reg.search(fileName)
        if ret == None:
            continue
        beforeDate = ret.group(1)
        month = ret.group(2)
        day = ret.group(4)
        year = ret.group(6)
        afterDate = ret.group(8)
        newFileName = beforeDate + day + '-' + month + '-' + year + afterDate
        print('Src File: ' + os.path.join(dirPath,fileName))
        print('New File:' + os.path.join(dirPath,newFileName))
        err = renameFile(os.path.join(dirPath,fileName), os.path.join(dirPath,newFileName))
        if err != None:
            print(err)
        
    

def renameFile(oldFileName, newFileName):
    if not os.path.isfile(oldFileName):
        return 'Not file name.'
    if not os.path.exists(oldFileName):
        return 'File ' + oldFileName + ' not exists.'
    
    shutil.move(oldFileName, newFileName)
    
def testRenameDir():
    renameDirFiles('.')
    
testRenameDir()
    
    
    
