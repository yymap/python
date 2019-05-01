#! python3

'''
fill word in file with place holders
'''

import os,re

def fillWord(fileName,holders):
    if not os.path.isfile(fileName) :
        print('Not file name')
        
    cwd = os.getcwd()
    print('cwd:'+ cwd)
    isFileExist = os.path.exists(fileName)
    if not isFileExist:
        fileName = os.path.join(cwd,fileName)
        isFileExist = os.path.exists(fileName)
    if not isFileExist :
        print('File not found.')
        return
    
    if holders == None :
        print('Holders can not been empty')
    
    f = open(fileName)
    fileContent = f.read()
    for h in holders :
        fileContent = re.sub(h, repl, string, count, flags)
    
    
    
        
