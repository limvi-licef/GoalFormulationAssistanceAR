# coding: utf-8


import cv2
import tkinter as tk
from PIL.Image import fromarray
from PIL.ImageTk import PhotoImage

from Tools.Singleton import Singleton

@Singleton
class GUI(tk.Tk):


    def __init__(self, debug=False):

        tk.Tk.__init__(self)
        self.debug = debug
        self.title("HoloGUI - " + ("Debug" if self.debug else "Release"))


    def display_video(self, canvas, frame):

        if self.isOpened():

            w = canvas.winfo_width()
            h = canvas.winfo_height()

            array = cv2.resize(frame, (w,h))
            img =  PhotoImage(image=fromarray(array))

            canvas.create_image(0,0, anchor="nw", image=img)

            return img


    def isOpened(self):

        try:
            self.update()
            return True
        except:
            return False


if __name__ == "__main__":

    video = cv2.VideoCapture("Cuisine_Salon-SalleAManger_Entrée_Chambre.mp4")

    win = GUI()
    video_canvas = tk.Canvas(win, width=640, height=360)
    video_canvas.pack(anchor=tk.W)

    while win.isOpened():
        
        r, frame = video.read()
        if r:
            displayed = win.display_video(video_canvas, frame[:,:,::-1])


