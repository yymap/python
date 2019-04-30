#! python3
import re

def runRegex(reg,tips) :
    txt = ''
    print(tips)
    while txt != 'exit' :
        txt = input()
        if(txt == 'exit') :
            break
        
        ret = reg.search(txt)
        if ret == None :
            print('Wrong! ' + tips)
            continue
        print('Right! It is ' + ret.group())
        print(tips)
    

def numberWithComma():
    
    tips = 'Enter the number str like 12,345,678 (Enter exit to quit):'
    reg = re.compile(r'^\d{1,3}(,\d{3})*$')

    runRegex(reg,tips)
   


def surName() :
    tips = 'Enter a full name(exit to quit):'
    reg = re.compile(r'^[A-Z][a-zA-Z]+ Eric$')

    runRegex(reg,tips)
        

def statement() :
    tips = 'Enter a statement like Alic/Bob/Carol eats/pets/throws apples/cats/baseballs.(exit to quit):'
    reg = re.compile(r'^(Alic|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs).$',re.I)

    runRegex(reg,tips)




def strongPwd() :
    tips = 'Enter a string pwd,lenth is at least 8, contain upper and lower letter, at least one number and special character.(Enter exit to quit):'
    reg = re.compile(r'^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*(?:\W|_))).{8,16}$')

    runRegex(reg,tips)

def strip2(txt,stripStr) :
    if stripStr == None :
        reg = re.compile(r'^\s*.*\s*$',re.DOTALL)    
    


def testRegex() :
    strongPwd()

testRegex()
        
        
