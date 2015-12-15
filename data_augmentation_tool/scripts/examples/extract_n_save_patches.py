#!/usr/bin/python

"""
loads img from folder and shows one image of each folder and then extract patch
"""
__author__ = 'Julia Nitsch'
import argparse
import data_augmentation_tool.io.load_images as io
import data_augmentation_tool.augmentation.transformations as transformation
import data_augmentation_tool.augmentation.normalization as normalization
import data_augmentation_tool.io.write_hdf5_file as write
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='''
    Test to load images, extract 5 patches per image and save them
    ''')
    parser.add_argument('--folder', help='folder where different classes are stored', default='')
    parser.add_argument('--filename', help='name of file which is stored', default='')

    args = parser.parse_args()
    folder = args.folder
    name = folder + args.filename


    images, labels, amount_classes = io.read_img_labels(folder)

    patch_size = 51

    # construct array for images
    shape_img = (5*len(images), 1, 51, 51)
    dt = np.float32
    img_np_array = np.empty(shape_img,dtype=dt)

    # construct array for label
    shape_label = (5*len(images), 1)
    label_np_array = np.empty(shape_label,dtype=dt)

    for img_idx, img in enumerate(images):
        for patch_idx in range(0,5):
            save_idx = img_idx * 5 + patch_idx
            patch = transformation.extract_patch_fliplr(images[patch_idx], 51)
            normalized_patch = normalization.std_normalization(patch)
            img_np_array[save_idx, 0, :, :] = normalized_patch
            label_np_array[save_idx,0] = labels[img_idx]

    print label_np_array

    write.write_dataset(name, img_np_array, label_np_array)



    print 'end'

if __name__ == "__main__":
    main()
