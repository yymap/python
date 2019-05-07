#! python3

'''
Bakup folder into zip file
'''

import os,zipfile


def backToZip():
    while True:
        print('Enter the folder to backup:')
        folderPath = input()
        if not os.path.isdir(folderPath):
            print('Should enter a folder path.')
            continue
        if not os.path.isabs(folderPath):
            print('Should enter absolute folder path.')
            continue
        break
    
    number = 1
    baseFolderName = os.path.basename(folderPath)
    while True:
        newZipFileName = baseFolderName + '_' + str(number) + '.zip'
        if os.path.exists(newZipFileName):
            number +=1
            continue
        break
    
    print('Generating %s...' % newZipFileName)
    zFile = zipfile.ZipFile(newZipFileName,'w')
    
    for currentFolder,subFolders,fileNames in os.walk(folderPath):
        print('Add files in folder '+currentFolder)
        zFile.write(currentFolder)
        
        for fName in fileNames:
            print('Add file '+ fName)
            zFile.write(os.path.join(currentFolder,fName))
    
    zFile.close()
    
    print('Done.')
    

backToZip()