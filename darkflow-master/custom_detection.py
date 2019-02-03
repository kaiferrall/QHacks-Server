#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 00:00:03 2019

@author: ameanasad
"""
#
#import cv2 
#from darkflow.net.build import TFNet 
#
#import numpy as np
#import time

import os 
import urllib.request as ulib
from bs4 import BeautifulSoup as bs
import random
import json
import requests
import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Liam is gay')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
print("Wassa")

#
#url_a = 'https://www.google.com/search?ei=1m7NWePfFYaGmQG51q7IBg&hl=en&q={}'
#url_b = '\&tbm=isch&ved=0ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ&start={}'
#url_c = '\&yv=2&vet=10ahUKEwjjovnD7sjWAhUGQyYKHTmrC2kQuT0I7gEoAQ.1m7NWePfFYaGmQG51q7IBg'
#url_d = '\.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'
#url_base = ''.join((url_a, url_b, url_c, url_d))

ua = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
]



url_base = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwit38zSwJXcAhWBwVkKHfeqB_gQ_AUICigB&biw=1366&bih=662"

def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, 0)
    cabecera = {"User-Agent": random.choice(ua)}
    req = requests.get(url, headers=cabecera )
    html = req.content
    soup = bs(html,"lxml")
    images = soup.find_all('div', {"class": 'rg_meta notranslate'})
    images = [i.text for i in images]
    images = [json.loads(i) for i in images]
    images = [images['ou'] for images in images]
    return images

if __name__ == '__main__' :
    
    search_name = 'guns'
    
    links = get_links(search_name)
    for link in links:
        print(link)
    
    