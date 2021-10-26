#! python3
import os,shutil,sys,pprint,pyperclip,webbrowser,requests,bs4,csv,json,time,datetime,subprocess,threading \
    ,smtplib,tkinter,shelve,smtplib,mime,email
from mime import mime_types
from typing import Text

    


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

''' demo: shelve
shFile = shelve.open('zy')


if 'tom' not in list(shFile.keys()):
    shFile['tom']={'name':'Tom Qin','age':'20'}
    print('tom added')
else:
    print(type(shFile['tom']))
    print('print tom')
    print(shFile['tom'])

shFile.close()
'''

''' demo: send mail
from email.mime.text import MIMEText
from email.header import Header

smtpServer = 'smtp.163.com'
smtpPort = 25
loginPwd = 'AAA'
sender = 'imap2000@163.com'
receiver = ['403681907@qq.com','zhaoyang2018@163.com']
smCharset = 'utf-8'

msg = MIMEText('this is python mail content....','plain',smCharset)
msg['Subject'] = Header('Python books subject2',smCharset)

msg['From'] = 'Eric<imap2000@163.com>' #Header('EricFrom',smCharset)  # use this will cause DT:SPM 163 error
msg['To'] = 'Tom<403681907@qq.com>' #Header('TomReceiver0',smCharset)

try:
    smObj = smtplib.SMTP()
    smObj.connect(smtpServer,smtpPort)
    smObj.login(sender,loginPwd)
    smObj.sendmail(sender,receiver,msg.as_string())
    print('Mail send success.')
    smObj.quit()
except smtplib.SMTPException as ex:
    print(ex)

'''







