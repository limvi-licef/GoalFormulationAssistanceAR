# coding: utf-8


from Lib.CameraSocket import CameraSocket
import Tools as tools
from GUI import GUI

import numpy as np
import tkinter as tk


############################################################################
class CameraGUI:

    ########################################################################
    def __init__(self):

        gui = GUI()

        self.canvas = tk.Canvas(gui, width=640, height=360)
        self.canvas.pack(anchor=tk.W)

        self.canvas.create_rectangle(0, 0, 640, 360, fill="black")
        self.canvas.update()


    ########################################################################
    def update(self, frame):

        self.displayed = GUI().display_video(self.canvas, frame)




############################################################################
@tools.Singleton
class Camera:

    """
    Receptor of frames from Hololens.
    
    Warning: Singleton.
    """

    debug_level = 0
    
    ########################################################################
    def __init__(self, host="127.0.0.1", port=9999):

        """
        Initialize connection status.
        """
        
        self.__connected = False
        self.socket = CameraSocket()
        self.connection(host, port)

        self.gui = CameraGUI()

        
    ########################################################################
    def isConnected(self):

        """
        Indicates connection status.
        """
        
        return self.__connected
    
    
    ########################################################################
    def connection(self, host, port):

        """
        Try to connect to Hololens.
        """
        
        if not self.isConnected():
            Camera.debug_level == 0 and print(f"Connection to Hololens on {host}:{port}")
        
            self.socket.Bind(host, port)
            self.__connected = self.socket.WaitConnection()
            
    
    ########################################################################
    def disconnect(self):

        """
        Stop connection to Hololens.
        """
        
        Camera.debug_level == 0 and print("Disconnection to Hololens")

        self.socket.Exit()
        self.socket.close()
        
    
    ########################################################################
    def updateFrame(self):

        """
        Request for frame to Hololens.
        """
        
        if self.__connected:
            Camera.debug_level == 1 and print("Frame catched")
            self.frame = self.socket.GetFrame()
            self.gui.update(self.frame)
        else:
            Camera.debug_level == 1 and print("Not connected to Hololens")
            
    
    ########################################################################
    def getFrame(self):

        """
        Return last received frame
        """
        
        if self.__connected:
            Camera.debug_level == 1 and print("Frame returned")
            return self.frame
        else:
            Camera.debug_level == 1 and print("Not connected to Hololens")
            return np.zeros((480,640,3), dtype=np.uint8)