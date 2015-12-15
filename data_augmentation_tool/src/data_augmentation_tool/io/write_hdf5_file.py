__author__ = 'jnitsch'
"""@package data_augmentation_tool.io.load_df5_data
Functions to write a file which is readable for caffe.

So the file contains the datasets /label and /data.
"""
import h5py
import numpy as np


def write_dataset(file_name, images, labels):

    # open file writeable
    file = h5py.File(file_name, "w")

    #create dataset for images
    dt_float32 = h5py.special_dtype(vlen=np.dtype('float32'))
    dset_img = file.create_dataset("/data", data=images)
    dset_label = file.create_dataset("/label", data=labels)

    file.close()
