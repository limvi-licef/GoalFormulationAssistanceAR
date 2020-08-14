# coding: utf-8


import sys
import os

FILE = os.path.abspath(__file__)
PATH, file = os.path.split(FILE)
PATH, contextual_assistance = os.path.split(PATH)

sys.path.append(PATH)