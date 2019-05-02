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
        print('Enter word for place holder %s' % h)
        replStr = input()
        fileContent = re.sub(r'\b%s\b' % h, replStr, fileContent)
    f.close()
    newFileName ='new_' + os.path.basename(fileName)
    newFile = open(newFileName,'w')
    newFile.write(fileContent)
    newFile.close()
    print('Replace completed.')
    
def testFillWord():
    fileContent = 'HAllo, this A new B comes A \n Let\'s A  go B and C then go to A B C, ok?'
    holders = ['A','B','C']
    fileName ='fillWordTest.txt'
    f = open(fileName,'w')
    f.write(fileContent)
    f.close()
    
    fillWord(fileName, holders)
    
testFillWord()
    
    
    
        
