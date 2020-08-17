# coding: utf-8


import cv2
import time

from Tools.Singleton import Singleton
from GUI import GUI

import tkinter as tk


############################################################################
@Singleton
class CameraEmul:

    ########################################################################
    def __init__(self, file):

        """
        Initialize connection status.
        """
        
        self.video = cv2.VideoCapture(file)

        gui = GUI()

        self.canvas = tk.Canvas(gui, width=640, height=360)
        self.canvas.pack(anchor=tk.W)

        self.canvas.create_rectangle(0, 0, 640, 360, fill="black")
        self.canvas.update()

        self._last_call = -1
        self.tic = int(1 / int(self.video.get(cv2.CAP_PROP_FPS)) * 1000)
        
    
    ########################################################################
    def updateFrame(self):

        if self._last_call == -1: self._last_call = time.time()

        tic = int((time.time() - self._last_call) * 1000)
        for t in range(max(tic//self.tic, 1)):
            self.readable, self.frame_src = self.video.read()
        self.frame = self.frame_src[:,:,::-1]

        self._last_call = time.time()
    

    ########################################################################
    def getFrame(self):

        self.displayed = GUI().display_video(self.canvas, self.frame)

        if self.readable:
            return self.frame
        else:
            return np.zeros((480,640,3), dtype=np.uint8)