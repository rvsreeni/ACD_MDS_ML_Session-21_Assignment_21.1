#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:28:49 2018

@author: macuser
"""
from bs4 import BeautifulSoup
import urllib.request
import nltk

response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,'html.parser')
print(soup.get_text())
print(type(soup))
letters = soup.find_all("div", class_="newscontent")

souptxt = ''
for cnt in range(len(letters)):
    print(letters[cnt].text)
    souptxt = souptxt + letters[cnt].text        
counts = nltk.FreqDist(souptxt.split())
print(counts)
print(counts.most_common(40))