# coding: utf-8


"""
    Python script for frame extraction.

    How to use:
        frame_extraction.py <VIDEO> <DIR>

        - VIDEO: path to video
        - DIR: directory path where frames will be placed.
"""


import sys

# Parse cmd line args
if len(sys.argv) == 3:
    _, VIDEO, DIR = sys.argv
else:
    print(__doc__)
    sys.exit(0)


import os
import cv2
import numpy as np

from add_lib_to_path import *
from Lib.lib import create_if_not_exists, progress_bar


def open_video(filename):

    """
        Open a cv2 video and return it with some properties (width, height, number of frame).
    """

    vid = cv2.VideoCapture(filename)

    prop = {}
    prop["width"] = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    prop["height"] = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    prop["frame_count"] = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

    return vid, prop


create_if_not_exists(DIR)

video, properties = open_video(VIDEO)
fcount = properties["frame_count"]

if not video.isOpened():
    print("Video opening failed")

else:
    
    for n in range(fcount): # for n from 0 to frame count

        readable, frame = video.read() # extract frame
        cv2.imwrite(f"{DIR}/{n}.jpg", frame) # save

        progress_bar(n+1, fcount) # update progress bar

