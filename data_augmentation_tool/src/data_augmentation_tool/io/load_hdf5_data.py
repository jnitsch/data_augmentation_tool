__author__ = 'jnitsch'
"""@package data_augmentation_tool.io.load_df5_data
Functions to load a file which is saved for being readable for caffe.

So the file contains the datasets /label and /data.
"""
import h5py


def load_hdf5_labels(filename):
    """Loads the labels of given file

    @param filename The absolute filename of the database.

    @return The read labels as list.
    """
    file_id = h5py.File(filename, 'r')
    label_set = file_id['/label']
    return label_set[:, 0]


def load_hdf5_img(filename):
    """Loads the data (images) of given file

    @param filename The absolute filename of the database.

    @return The read images as list.
    """
    file_id = h5py.File(filename, 'r')
    img_set = file_id['/data']
    return img_set


def print_dimensions(filename, dataset):
    file_id = h5py.File(filename, 'r')
    dset = file_id[dataset]
    print 'Dataset %s has dimension %d' % dataset, dset.shape
