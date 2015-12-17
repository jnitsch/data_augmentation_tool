#!/usr/bin/python

"""
This script loads images from given folder which has following structure:
 /folder
    --/class_0
    --/--/img_0
    --/--/img_
    --/--/...
    --/class_1
    --/--/img_0
    --/--/img_1
    --/...
It performs simple data augmentation on the images and extracts patches with defined size. The augmented data is then
stored in the defined file containing a /data and a /label dataset. This datasets have the 'right' dimensions for caffe
and can be directly used for learning. The amount of samples per image is defined through an argument.
"""
__author__ = 'Julia Nitsch'
import argparse
from argparse import RawTextHelpFormatter
import data_augmentation_tool.io.load_images as io
import data_augmentation_tool.augmentation.transformations as transformation
import data_augmentation_tool.augmentation.normalization as normalization
import data_augmentation_tool.io.write_hdf5_file as write
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='''
    This script loads images from given folder which has following structure:
     /folder
        --/class_0
        --/--/img_0
        --/--/img_1
        --/--/...
        --/class_1
        --/--/img_0
        --/--/img_1
        --/...
    It performs simple data augmentation on the images and extracts patches with defined size. The augmented data is then
    stored in the defined file containing a /data and a /label dataset. This datasets have the 'right' dimensions for caffe
    and can be directly used for learning. The amount of samples per image is defined through an argument.
    !!! WARNING
    Use this script iff you have a small amount of data and/or small amount of patches. Otherwise it is likely that you run
    out of memory (RAM)!!!
    ''', formatter_class=RawTextHelpFormatter)
    parser.add_argument('--folder', help='folder where different classes are stored', default='')
    parser.add_argument('--filename', help='name of file which is stored', default='')
    parser.add_argument('--patchsize', help='size of patch which will be extracted', default=51)
    parser.add_argument('--samples_per_img', help='amount of samples which should be taken per image', default=100)

    args = parser.parse_args()
    folder = args.folder
    name = folder + args.filename
    patch_size = int(args.patchsize)
    samples_per_img = int(args.samples_per_img)

    # read in images
    images, labels, amount_classes = io.read_img_labels(folder)

    # construct array for images [#images, #channels, width, height]
    shape_img = (samples_per_img*len(images), 1, patch_size, patch_size)
    dt = np.float32
    img_np_array = np.empty(shape_img,dtype=dt)

    # construct array for label
    shape_label = (samples_per_img*len(images), 1)
    label_np_array = np.empty(shape_label,dtype=dt)

    # perform augmentation
    for img_idx, img in enumerate(images):
        for patch_idx in range(0,samples_per_img):
            # compute current idx
            save_idx = img_idx * samples_per_img + patch_idx
            # extract patch
            patch = transformation.extract_patch_fliplr(images[patch_idx], patch_size)
            # normalize patch
            normalized_patch = normalization.std_normalization(patch)
            # save stuff in datastructure
            img_np_array[save_idx, 0, :, :] = normalized_patch
            label_np_array[save_idx,0] = labels[img_idx]


    # write it to file
    write.write_dataset(name, img_np_array, label_np_array)



    print 'Finished!'

if __name__ == "__main__":
    main()
