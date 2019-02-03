#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 00:19:30 2019

@author: ameanasad
"""

import os 

imdir = 'images'

if not os.path.isdir(imdir):
    os.mkdir(imdir)
    


pistol_folders = [folder for folder in os.listdir('dataset') if 'pistol' in folder]




n = 0

for folder in pistol_folders:
    
    for imfile in os.scandir('dataset/' + folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n +=1
        
        