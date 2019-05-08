#! python3
'''
Use search engine easily
'''

import webbrowser,requests,bs4,logging
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def baiduSearch(keyWord,topCount):
    baseUrl = 'http://www.baidu.com/s?wd=' + keyWord
    res = requests.get(baseUrl)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    tags = soup.select('div.result.c-container h3 a[data-click]')
    openLinkCount = min(topCount,len(tags))
    for i in range(openLinkCount):
        logging.debug(tags[i].get('href'))
        webbrowser.open(tags[i].get('href'))
    
# baiduSearch('python', 5)


'''
You need to download chromedriver.exe from google .
Then copy it into chrome installation directory, like C:\Program Files (x86)\Google\Chrome\Application
Then add this path into system envrionment variable: path.
'''
def operChrome():
    chromeBrowser = webdriver.Chrome()
    baseUrl = 'https://www.cnblogs.com/pick/'
    chromeBrowser.get(baseUrl)
    

operChrome()
