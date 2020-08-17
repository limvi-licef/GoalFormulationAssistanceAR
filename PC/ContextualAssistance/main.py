# coding: utf-8

from add_lib_to_path import *

import InputOutput as io
import Ontology as onto
import DecisionKernel as dk
import Context as ctx
import CustomAssistanceLevel as cal
import Tools as tools
from GUI import GUI

import cv2
import tkinter as tk


def main(debug=False):

    ONTO_PATH = "Ontology\\GoalOntoV1.owl"

    MODEL = "model"
      
    win = GUI(debug)
    win.update()

    cam = io.Camera(host="192.168.1.21", port=9999)
    #cam = tools.CameraEmul("train_test.mp4")
    
    outputStack = io.OutputStack(host="192.168.1.21", port=9998)
    goalOnto = onto.GoalOnto(ONTO_PATH)
    roomClassification = ctx.RoomClassification(MODEL, 20)
    clockTime = ctx.ClockTime()
    assistanceLevel = cal.TextAssistance()
    decisionKernel = dk.GoalDecisionKernel(goalOnto, assistanceLevel)
    decisionKernel.add(roomClassification, clockTime)

    while win.isOpened():

        for _ in range(1): cam.updateFrame()
        decisionKernel.update()


if __name__ == "__main__":

    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "-d": main(debug=True)
    else: main()