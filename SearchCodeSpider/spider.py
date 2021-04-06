import requests
import re
import urllib.request
from bs4 import BeautifulSoup
from distutils.filelist import findall




def getmaxpage(key):
    page=0
    maxpage=0
    hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    html = requests.get('https://searchcode.com/?q=%22'+key+'%22&p='+str(page),headers = hea)
    html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
    filename = open('write.html', 'w', encoding="utf-8")
    filename.write(html.text)
    try:
        soup = BeautifulSoup(open('write.html','r', encoding='UTF-8'))
        for tag in soup.find_all('span', class_='page'):
            maxpage=tag.get_text()
        return maxpage
    except ValueError:
        return -1

def writetofile(key,li=[]):
    filename=key+".txt"
    print(filename)
    with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for i in li:
            f.write(i)
            f.write('\n')



def spider(key):
    page=0
    result=[]
    hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    maxpage=int(getmaxpage(key))-int(1)
    if maxpage>=0:
        while int(page) <= int(maxpage): 
            html = requests.get('https://searchcode.com/?q=%22'+key+'%22&p='+str(page),headers = hea)
            html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
            filename = open('write.html', 'w', encoding="utf-8")
            filename.write(html.text)
            soup = BeautifulSoup(open('write.html','r', encoding='UTF-8'))
            for div in soup.find_all('div',style='width:100%;'):
                for url in div.find_all('small'):
                    result.append(url.get_text())
            page=page+1
        writetofile(key,result)
    else:
        return 0

f=open("keyword.txt")
line=f.readlines()
keylist=[]
for i in line:
    rs = i.rstrip('\n')  # 移除行尾换行符
    keylist.append(rs)
for i in keylist:
    spider(i)
