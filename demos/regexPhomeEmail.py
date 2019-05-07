#! python3
# the mobile is US mobile

import re, pyperclip

def getPhone(text) :
    reg = re.compile(r'''(
                    (\d{3}|\(\d{3}\))?   # area code
                    (\s|-|\.)?     #separator
                    (\d{3})   #  first 3 digits
                    (\s|-|\.)  # separator
                    (\d{4})   # last 4 digits
                    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension
                    )''', re.VERBOSE)
    return reg.findall(text)

def getMail(text) :
    reg = re.compile(r'''(
                [\w.]+
                @
                [\w]+
                (\.[a-zA-Z0-9]{2,4})
                )''',re.VERBOSE)
    return reg.findall(text)



def getRegexResult() :
    tips = 'Enter ok to execute regex(enter exit to quit):'
    text = ''
    while text != 'exit' :
        print(tips)
        text = input()
        if text == 'exit' :
            break
        if text != 'ok' :
            print(tips)
            continue
        text = pyperclip.paste()
        phoneList = getPhone(text)
        print('******Phone list is :')
        for s in phoneList :
            print(s[0])

        print('******Email list is :')
        emailList = getMail(text)
        for s in emailList :
            print(s[0])
        

    



getRegexResult()
    
    
