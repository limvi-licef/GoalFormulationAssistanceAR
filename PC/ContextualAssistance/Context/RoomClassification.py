# coding: utf-8


import numpy as np
import tkinter as tk

import Tools as tools
from Lib.lib import calc_hist
import InputOutput as io

from Context.Indicator import Indicator
from GUI import GUI


##########################################################################
class RoomClassificationGui(tk.Frame):

    """
    GUI for room classification class.
    """

    def __init__(self):

        gui = GUI()
        tk.Frame.__init__(self, )

        self.title = tk.Label(self, text="Room classification loading", font=('Arial', 16))
        self.title.pack(anchor=tk.W)

        self.detected = tk.Label(self, text="", font=('Arial', 12))
        self.detected.pack(anchor=tk.W)

        self.pack(anchor=tk.W)
        gui.update()


##########################################################################
class RoomClassification(Indicator):

    """
    Context indicator of current user room using predictive model.
    """

    ######################################################################
    def __init__(self, model, frame_count):

        """
        Setup prediction model.
        """

        self.gui = RoomClassificationGui()

        from tensorflow.keras.models import load_model

        Indicator.__init__(self)
        self._model = load_model(model+".h5")
        self._classes = np.load(model+"_classes.npy")
        self._frame_count = frame_count

        self._h = 0
        self._hist = np.zeros((self._frame_count,3,256), dtype=np.float32)

        self.gui.title['text'] = "Room classification"
        self.gui.detected['text'] = "Detected: None"

    
    ######################################################################
    def run(self):

        """
        Return updated indicator.
        """
        
        if self._h < self._frame_count:

            frame = tools.CameraEmul().getFrame()
            frame = io.Camera().getFrame()

            self._hist[self._h,:,:] = calc_hist([frame], bins=256)
            self._h += 1

            return self._indicator
        
        else:

            self._h = 0

            probs = self._model.predict(self._hist)
            preds = np.argmax(probs, axis=1)
            pred_hist = np.bincount(preds)

            pred = np.argmax(pred_hist)
            pred = self._classes[pred]

            self.gui.detected['text'] = f"Detected: {pred}"

            return pred

