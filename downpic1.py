﻿# -*- coding: utf-8 -*-
"""
Spyder Editor
getpages.py
This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os

#url = 'http://localhost/test'

def getpic(page):
    piclink = []
    ress = requests.get(page)
    ress.encoding = 'utf-8'
    soup = BeautifulSoup(ress.text,'html.parser')
    #print (soup.title.text)
    name = soup.title.text
    #soup = soup.find_all('img') 
    soup = soup.find_all("img",class_="content_img")
    for list in soup:    
        #link = list.find('img')
        link = list.get('src')
        #print (type(link))
        #print(link)
        piclink.append('http://127.0.0.1/test/'+link)
    return piclink,name 

def downpic(links):
    for i in links:
        r = requests.get(i)
        pic = i.split("/",)[-1]                     #get file name
        with open(pic,"wb") as code:
            code.write(r.content)
            print(pic+" is down!")


url = 'http://localhost/test/i2.htm'

(links,name) = getpic(url)

#print(os.path.exists(name))

if not os.path.exists(name):
    os.mkdir(name)
    os.chdir(name)
    print(name+" 目录不存在,begin to make it")
    
else:
    os.chdir(name)
    print(name+" 目录已经存在")
    

downpic(links)

os.chdir('../')
