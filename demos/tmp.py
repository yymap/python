#! python3
import os,shutil,sys,pprint,pyperclip,webbrowser,requests,bs4,csv,json,time,datetime,subprocess,threading \
    ,smtplib,tkinter,shelve

''' demo1
try:
    res = requests.get('http://cn.bingaa.com/')
    res.raise_for_status()
except Exception as err:
    print('there is an error: %s' % (err))

print(res.status_code)
print('response length: %s' % len(res.text))

print(res.text[:200])
'''

'''  demo2
os.environ['NO_PROXY']='cnblogs.com'

try:
    res = requests.get('https://www.cnblogs.com/chenssy/p/15440348.html',stream=True,verify=False)
    res.raise_for_status()
    saveFile = open(r'.\tmp\nio.html','wb')
    totalCount = 0
    for chunk in res.iter_content(100000):
        totalCount += saveFile.write(chunk)
    saveFile.close()

    res.close()
    print('Total count :%s' % (totalCount))
except Exception as err:
    print('get error: %s' % (err))
    sys.exit(1)
'''

shFile = shelve.open('zy')


if 'tom' not in list(shFile.keys()):
    shFile['tom']={'name':'Tom Qin','age':'20'}
    print('tom added')
else:
    print(type(shFile['tom']))
    print('print tom')
    print(shFile['tom'])

shFile.close()








