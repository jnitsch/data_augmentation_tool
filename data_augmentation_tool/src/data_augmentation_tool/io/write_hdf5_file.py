__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.io.load_df5_data
Functions to write a file which is readable for caffe.

So the file contains the datasets /label and /data.
"""
import h5py
import numpy as np
import os


def create_database(file_name, patch_size, channels):
    # delete file if already exists
    try:
        os.remove(file_name)
    except OSError:
        pass

    # open file writeable
    file = h5py.File(file_name, "w")

    #create dataset for images
    dt_float32 = h5py.special_dtype(vlen=np.dtype('float32'))

    dset_img = file.create_dataset("/data", (0,channels, patch_size, patch_size), maxshape=(None, channels, patch_size, patch_size), dtype=dt_float32)
    dset_label = file.create_dataset("/label", (0, 1), maxshape=(None, 1), dtype=dt_float32)

    return file, dset_img, dset_label


def extend_img(dset, data):
    start_idx = dset.shape[0]
    # resized shape
    shape = list(data.shape)
    shape[0] = shape[0] + start_idx
    dset.resize(shape)
    end_idx = dset.shape[0]
    for idx in range(start_idx,end_idx):
        dset[idx,0,:,:] = data[idx-start_idx,0,:,:]


def extend_labels(dset, data):
    start_idx = dset.shape[0]
    # resized shape
    shape = list(data.shape)
    shape[0] = shape[0] + start_idx
    dset.resize(shape)
    end_idx = dset.shape[0] - 1
    dset[start_idx:end_idx,0] = data[:,0]


def write_dataset(file_name, images, labels):
    """Writes the whole database at once.

    This function creates the file and writes the whole database at once. Don't use this functionality if you have
    big data. This leads to huge memory (RAM) usage.

    @param file_name The filename of the database.
    @param images NumPy array with images
    @param labals NumPy array containing the labels
    """

    # delete file if already exists
    try:
        os.remove(file_name)
    except OSError:
        pass

    # open file writeable
    file = h5py.File(file_name, "w")

    #create dataset for images
    dt_float32 = h5py.special_dtype(vlen=np.dtype('float32'))
    dset_img = file.create_dataset("/data", data=images)
    dset_label = file.create_dataset("/label", data=labels)

    file.close()
