#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:35:10 2019

@author: ameanasad
"""

import cv2
import sys
sys.path.insert(0, "/Users/ameanasad/Documents/Queen's/2018:2019/qhacks/darkflow-master")

from darkflow.net.build import TFNet 

import numpy as np
import time
              

class VideoCamera(object):
    def __init__(self):
      
        self.option = {
            
            'model' : "/Users/ameanasad/Documents/Queen's/2018:2019/qhacks/darkflow-master/cfg/yolo.cfg",
            'load':  "/Users/ameanasad/Documents/Queen's/2018:2019/qhacks/darkflow-master/bin/yolov2.weights",
            'threshold': 0.4
            
            }
        
        self.tfnet = TFNet(self.option)
        self.result_dic ={}


    def __del__(self):
        self.video.release()

    def get_frame(self):
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
        colors = [tuple(255*np.random.rand(3)) for i in range(10)]

            
        
        
        img = cv2.imread('crowd.jpg', cv2.IMREAD_COLOR)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        result = self.tfnet.return_predict(img)
        
        print(result)
        for x in range(len(result)):
    
            tl = (result[x]['topleft']['x'], result[x]['topleft']['y'])
            br = (result[x]['bottomright']['x'], result[x]['bottomright']['y'])
            label = result[x]['label']


            img = cv2.rectangle(img, tl, br, (0,255,0), 7)
            img = cv2.putText(img, label, tl,cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
        
        self.result_dic = {}
        

            

        ret, jpeg = cv2.imencode('.png', img)

        return self.result_dic, jpeg.tobytes()

    def get_results(self):
        return self.result_dic
