#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:20:37 2019

@author: ameanasad
"""

import os
import matplotlib  
from matplotlib.pyplot import ion, draw,show
#matplotlib.use('TkAgg', warn=False, force = True)

import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from create_annotations import write_xml

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = 'sample_img/'
savedir = 'annotations'
obj = 'pistol'

def line_select_callback(eclick, erelease):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(eclick.xdata), int(eclick.ydata)))
    br_list.append((int(erelease.xdata), int(erelease.ydata)))
    object_list.append(obj)


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        
        print(object_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        
        plt.close()
    
    return True
def toggle_selector(event):
    toggle_selector.RS.set_active(True)



f = (list(enumerate(os.scandir(image_folder))))
print(f)
for n, image_file in f:
    print(image_file)
    img = image_file
    fig, ax = plt.subplots(1)
#        mngr = plt.get_current_fig_manager()
#        mngr.window.setGeometry(250, 120, 1280, 1024)
    
    
           
    image = cv2.imread(image_file.path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ax.imshow(image)
    toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True
        )
    bbox = plt.connect('key_press_event', toggle_selector)
    keypress =  plt.connect('key_press_event', onkeypress)
    print(bbox)
    time.sl
    plt.show()
    
       
  