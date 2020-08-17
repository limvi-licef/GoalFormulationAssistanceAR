# coding: utf-8


"""
    Train a model.

    How to use:
        train_model.py <MODEL> <DATA> <BINS> <EPOCH>

        - MODEL: model directory
        - DATA: directory path to images
        - BINS: bins per color channel
        - EPOCH: total number of epoch (1 batch per epoch)
"""


import sys

# Parse cmd line args
if len(sys.argv) == 5:
    _, NAME, DATA, BINS, EPOCH = sys.argv
else:
    print(__doc__)
    sys.exit(0)


import os
import time
import json
import numpy as np
import tensorflow as tf

from add_lib_to_path import *
from Lib.lib import calc_hist


data = tf.keras.preprocessing.image.DirectoryIterator(
    DATA,
    tf.keras.preprocessing.image.ImageDataGenerator(dtype=np.uint8),
    target_size=(640,360),
    class_mode='sparse',
    batch_size=100,
    dtype=np.uint8
    )


model = tf.keras.models.load_model(NAME)


model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss=tf.keras.losses.sparse_categorical_crossentropy,
    metrics=["accuracy"]
    )

t = str(int(time.time()))
basename, modelname = os.path.split(NAME)
training_logfile = tf.summary.create_file_writer(basename+"/logs_"+t)


with training_logfile.as_default():
    for n, (images, labels) in enumerate(data):
    
        histograms = calc_hist(images, int(BINS), print_trace=True)

        training = model.fit(histograms, labels, batch_size=32, epochs=1)
        tf.summary.scalar("loss", training.history['loss'][0], step=n)
        tf.summary.scalar("accuracy", training.history['accuracy'][0], step=n)

        if n==int(EPOCH): break

model.save(basename+"/model_"+t+".h5")
np.save(basename+"/classes.npy", os.listdir(DATA))

