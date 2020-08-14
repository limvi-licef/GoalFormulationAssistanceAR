# coding: utf-8


import cv2
import numpy as np


##########################################################################
HIST_BINS = 24


##########################################################################
def normalize(h):

    return (h - h.min()) / (h.max() - h.min())


##########################################################################
def build_hist_hsv(images):

    hist = np.zeros((len(images),HIST_BINS*3), dtype=np.float32)

    for n, image in enumerate(images):
        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

        hist_h, _ = np.histogram(hsv[:,:,0], bins=HIST_BINS)
        hist_s, _ = np.histogram(hsv[:,:,1], bins=HIST_BINS)
        hist_v, _ = np.histogram(hsv[:,:,2], bins=HIST_BINS)

        hist[n, HIST_BINS*0:HIST_BINS*1] = normalize(hist_h)
        hist[n, HIST_BINS*1:HIST_BINS*2] = normalize(hist_s)
        hist[n, HIST_BINS*2:HIST_BINS*3] = normalize(hist_v)

    return hist


##########################################################################
def add_hist_hsv(hist, n, image):

    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    hist_h, _ = np.histogram(hsv[:,:,0], bins=HIST_BINS)
    hist_s, _ = np.histogram(hsv[:,:,1], bins=HIST_BINS)
    hist_v, _ = np.histogram(hsv[:,:,2], bins=HIST_BINS)

    hist[n, HIST_BINS*0:HIST_BINS*1] = normalize(hist_h)
    hist[n, HIST_BINS*1:HIST_BINS*2] = normalize(hist_s)
    hist[n, HIST_BINS*2:HIST_BINS*3] = normalize(hist_v)