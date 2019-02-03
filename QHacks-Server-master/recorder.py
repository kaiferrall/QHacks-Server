import sys
import cv2
import numpy as np
import time
import base64
sys.path.insert(0, r'C:\Users\kaife\Documents\qHacks\darkflow-master')
from darkflow.net.build import TFNet


class VideoCamera2(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        self.option = {

            'model': r'C:\Users\kaife\Documents\qHacks\darkflow-master\cfg\yolo.cfg',
            'load':  r'C:\Users\kaife\Documents\qHacks\darkflow-master\bin\yolov2.weights',
            'threshold': 0.4

        }

        self.tfnet = TFNet(self.option)
        self.result_dic = {}

    def __del__(self):
        self.video.release()

    def get_frame(self):
        #self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        #self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1920)
        colors = [tuple(255*np.random.rand(3)) for i in range(10)]

        stime = time.time()

        ret, frame = self.video.read()

        results = self.tfnet.return_predict(frame)

        self.result_dic = {}
        if ret:
            for color, result in zip(colors, results):

                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                try:
                    self.result_dic[label] += 1
                except KeyError:
                    self.result_dic[label] = 1
                confidence = result['confidence']

                text = '{}: {:.0f}%'.format(label, confidence*100)

                frame = cv2.rectangle(frame, tl, br, color, 4)
                text = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 0), 2)

#                cv2.imshow('frame', frame)
            print("FPS {:.1f}".format(1/(time.time()-stime)))
            print("Frame Results: \n")
            print(self.result_dic)

        ret, jpeg = cv2.imencode('.jpg', frame)

        return (self.result_dic, jpeg.tobytes())

    def get_results(self):
        return self.result_dic
