# coding: utf-8


import os
import cv2
import numpy as np
import tensorflow as tf


##########################################################################
def create_if_not_exists(path):

    """
        Creates a directory for extracted frames.
    """

    try:
        os.mkdir(path)
        return True
    except:
        return False


##########################################################################
def progress_bar(bar_value, bar_range):

    """
        Progress bar displayed in console.
    """

    n = bar_value * 30 // bar_range

    bar = "[" + "#"*n + " "*(30-n) + f"] {bar_value}/{bar_range}"

    if bar_value == bar_range: print(bar, end='\n')
    else: print(bar, end='\r')


##########################################################################
def normalization(h):

    """
        Return an array whith normlized values.
    """

    return (h - h.min()) / (h.max() - h.min())


##########################################################################
def calc_hist(images, bins=256, normalize=True, print_trace=False):

    """
        Convert each image to hsv color mode and build its histogram.
    """

    hist = np.zeros((len(images),3,256))

    for n, image in enumerate(images):

        i = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        for c in range(3):
            hist[n,c,:] = tf.math.bincount(i[:,:,c], minlength=bins, maxlength=bins)
        if print_trace: progress_bar(n+1, len(images))

    if normalize:
        return normalization(hist)
    else:
        return hist



