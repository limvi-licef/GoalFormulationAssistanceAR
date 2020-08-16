# coding: utf-8


"""
    Build a new model.

    How to use:
        create_model.py <NAME> <BINS> <CLASSES>

        - NAME: model filename
        - BINS: bins per color channel
        - CLASSES: number of class to classify
"""


import sys

# Parse cmd line args
if len(sys.argv) == 4:
    _, NAME, BINS, CLASSES = sys.argv
else:
    print(__doc__)
    sys.exit(0)

import json
import tensorflow as tf
from lib import create_if_not_exists


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(3,256)),
    tf.keras.layers.Dense(int(CLASSES), activation=tf.keras.activations.softmax),
])


create_if_not_exists(NAME)
model.save(NAME+"/model_empty.h5")

