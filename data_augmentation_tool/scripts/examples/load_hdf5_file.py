#!/usr/bin/python

"""
loads hdf5 caffe file and shows one single image of each label
"""
__author__ = 'Julia Nitsch'
import argparse

import data_augmentation_tool.io.load_hdf5_data as io
import data_augmentation_tool.utils.visualization as util


def main():
    parser = argparse.ArgumentParser(description='''
    Test to load images and visualize one of each class
    ''')
    parser.add_argument('--filename', help='path+filename of hdf5 file', default='')
    parser.add_argument('--amount_classes', help='amount of different classes which are expected', default='')
    args = parser.parse_args()
    filename = args.filename
    amount_classes = int(args.amount_classes)

    label = io.load_hdf5_labels(filename)
    img = io.load_hdf5_img(filename)


    if img.shape[1] is 1:
        print 'Images are grayscale'


    if img.shape[1] is 3:
        print 'Images are colorized'

    for label_it in range(0,amount_classes):
        idx = label.tolist().index(label_it)
        window_name = 'Label ' + str(label_it)
        util.show_single_img_named(img[idx,0,:,:], window_name)

if __name__ == "__main__":
    main()