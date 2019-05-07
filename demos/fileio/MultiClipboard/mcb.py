#! python3
'''
mcb.pyw  save and load pieces of text to clipboard
usage:
py.exe mcb.pyw save <keyword>  save clipboard to keyword
py.exe mcb.pyw <keyword>  load keyword to clipboard
py.exe mcb.pyw list   load all keywords to clipboard

'''

import shelve, pyperclip, sys

def mcb() :
    mcbFile = shelve.open('mcb')

    # save clipboard content
    if len(sys.argv) == 3 :
        if sys.argv[1].lower() == 'save' :
            mcbFile[sys.argv[2]] = pyperclip.paste()
        elif sys.argv[1].lower() == 'delete' :
            if sys.argv[2] in mcbFile :
                del mcbFile[sys.argv[2]]
        
    elif len(sys.argv) == 2 :
        if sys.argv[1].lower() == 'list' :
            pyperclip.copy(str(list(mcbFile.keys() )))
        elif sys.argv[1].lower() == 'delete' :
            del mcbFile
        elif sys.argv[1] in mcbFile :
            pyperclip.copy(mcbFile[sys.argv[1]] )
            
    mcbFile.close()


def testMcb() :
    mcb()

testMcb()
