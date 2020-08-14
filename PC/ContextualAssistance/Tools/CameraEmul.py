# coding: utf-8


import cv2

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
        
    
    ########################################################################
    def updateFrame(self):
        
        self.readable, self.frame_src = self.video.read()
        self.frame = self.frame_src[:,:,::-1]
    

    ########################################################################
    def getFrame(self):

        self.displayed = GUI().display_video(self.canvas, self.frame)

        return self.readable, self.frame