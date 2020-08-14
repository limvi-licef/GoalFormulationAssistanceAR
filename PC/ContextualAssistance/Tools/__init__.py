# coding: utf-8


"""
App package for common code and extra tools such as emulation.
"""


from Tools.CameraEmul import CameraEmul
from Tools.Singleton import Singleton

from Tools.histogram import build_hist_hsv, add_hist_hsv, HIST_BINS