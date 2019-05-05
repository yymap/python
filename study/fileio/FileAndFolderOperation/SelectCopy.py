#! python3
'''
Copy a folder to another place, and it will skip folders whose name starts with your input arguments
For example: you want to copy all folders to another place except for .git folders
'''

import os,shutil

def copyFolder():
    
    while True:
        print('Enter src folder path:')
        srcFolder = input()
        if not os.path.isdir(srcFolder):
            print('Invalid src folder, must be a directory path.')
            continue
        if not os.path.exists(srcFolder):
            print('Src folder path not exists')
            continue
        if not os.path.isabs(srcFolder):
            print('Should be absolute src path.')
            continue
        break
    
    while True:
        print('Enter src dest path:')
        destFolder = input()
        if not os.path.isdir(destFolder):
            print('Invalid dest folder, must be a directory path.')
            continue
        if not os.path.exists(destFolder):
            print('Dest folder path not exists')
            continue
        if not os.path.isabs(destFolder):
            print('Should be absolute dest path.')
            continue
        break
    
    print('Enter filter folder name prefix:')
    filterPrefix = input()
    
    print('Begin copying,please waiting...')
    copyFolderCore(srcFolder,destFolder,filterPrefix)
    print('Copy completed.')

def copyFolderCore(absSrcFolderPath, absDestFolderPath, filterPrefix):
    needFilter = (filterPrefix != None and len(filterPrefix) > 0)
    
    for itemName in os.listdir(absSrcFolderPath):
        
        srcPath = os.path.join(absSrcFolderPath,itemName)
        destPath = absDestFolderPath
        
        if os.path.exists(os.path.join(destPath,itemName)):
            continue
        
        if not os.path.exists(destPath):
            os.makedirs(destPath)
        
        # File not filter
        if not os.path.isdir(srcPath):
            shutil.copy(srcPath, destPath)
            continue
            
        if needFilter and itemName.startswith(filterPrefix):
            continue
        
        for subItemName in os.listdir(srcPath):
            srcPath = os.path.join(absSrcFolderPath,itemName,subItemName)
            destPath = os.path.join(absDestFolderPath,itemName)
            
            if os.path.exists(os.path.join(destPath,subItemName)):
                continue
            
            if not os.path.exists(destPath):
                os.makedirs(destPath)
            
            if not os.path.isdir(srcPath):
                shutil.copy(srcPath, destPath)
                continue
            
            if needFilter and subItemName.startswith(filterPrefix):
                continue
            
            destPath = os.path.join(absDestFolderPath,itemName,subItemName)
            shutil.copytree(srcPath,destPath)
            print('Folder ' + srcPath + ' copied ....')
            


copyFolder()
    
        
    
