# Model directory

Scripts for model setup are here.
Use them with Anaconda prompt.


## Frame extraction

Extract all frames from a video.

    python frame_extraction.py <VIDEO> <DIR>

* VIDEO: path to video file.
* DIR: directory path where frames will be placed.


## Create model

Build a new model and save it into h5 file.

    create_model.py <NAME> <BINS> <CLASSES>

* NAME: model filename.
* BINS: bins per color channel.
* CLASSES: number of class to classify.


## Train model

Train a model.

    train_model.py <MODEL> <DATA> <BINS> <EPOCH>

* MODEL: model file.
* DATA: directory path to images.
* BINS: bins per color channel.
* EPOCH: total number of epoch (1 batch per epoch).


## Run model

Run model on a video.

    run_model.py <MODEL> <VIDEO>

* MODEL: model path
* VIDEO: video path