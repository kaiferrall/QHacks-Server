#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:49:20 2019

@author: ameanasad
"""

import cv2
from darkflow.net.build import TFNet

import matplotlib.pyplot as plt

#%config InlineBackend.figure_format = 'svg'


options = {
        'model' : 'cfg/yolo.cfg',
        'load' : 'bin/yolov2.weights',
        'threshold': 0.4,
        
        }


tfnet = TFNet(options)


img = cv2.imread('crowd.jpg', cv2.IMREAD_COLOR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

result = tfnet.return_predict(img)

print(result)
for x in range(len(result)):
    
    tl = (result[x]['topleft']['x'], result[x]['topleft']['y'])
    br = (result[x]['bottomright']['x'], result[x]['bottomright']['y'])
    label = result[x]['label']


    img = cv2.rectangle(img, tl, br, (0,255,0), 7)
    img = cv2.putText(img, label, tl,cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

plt.imshow(img)
plt.show

