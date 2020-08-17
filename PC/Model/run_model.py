# coding: utf-8


"""
    Run model on a video.

    How to use:
        run_model.py <MODEL> <VIDEO>

        - MODEL: model path
        - VIDEO: video path
"""


import sys

# Parse cmd line args
if len(sys.argv) == 3:
    _, MODEL, VIDEO = sys.argv
else:
    print(__doc__)
    sys.exit(0)


import cv2
import numpy as np
from tensorflow.keras.models import load_model

from add_lib_to_path import *
from Lib.lib import calc_hist


basename, modelname = os.path.split(MODEL)
classes = np.load(basename+"/classes.npy")

video = cv2.VideoCapture(VIDEO)
model = load_model(MODEL)

while video.isOpened():

    readable, frame = video.read()

    if readable:

        histogram = calc_hist([frame[:,:,::-1]], bins=256)
        pred = np.argmax(model.predict(histogram))

        cv2.imshow("", frame)
        if cv2.waitKey(1) == ord('q'): break

        print(classes[pred])

