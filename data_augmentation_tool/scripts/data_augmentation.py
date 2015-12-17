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
It performs data augmentation [rotate img randomly, scales it randomly bewteen 90% and 110%] on the images and
extracts patches with defined size and normalizes it. The augmented data is then
stored in the defined file containing a /data and a /label dataset. This datasets have the 'right' dimensions for caffe
and can be directly used for learning. The amount of samples per image is defined through an argument.
"""
__author__ = 'Julia Nitsch'
import argparse
from argparse import RawTextHelpFormatter
import data_augmentation_tool.io.load_images as io
import data_augmentation_tool.io.load_hdf5_data as io_h5
import data_augmentation_tool.augmentation.transformations as transformation
import data_augmentation_tool.augmentation.normalization as normalization
import data_augmentation_tool.io.write_hdf5_file as write
import data_augmentation_tool.utils.visualization as viz
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="""
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
    It performs data augmentation [rotate img randomly, scales it randomly bewteen 90% and 110%] on the images and
    extracts patches with defined size and normalizes it. The augmented data is then
    stored in the defined file containing a /data and a /label dataset. This datasets have the 'right' dimensions for caffe
    and can be directly used for learning. The amount of samples per image is defined through an argument. This script
    can handle a huge amount of data BUT is VERY SLOW!
    """, formatter_class=RawTextHelpFormatter)
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

    # construct file
    file, dset_img, dset_label = write.create_database(name, patch_size, 1)

    # datatype used to store data
    dt = np.float32

    # size of datat blocks which are written to file
    shape_img = (samples_per_img, 1, patch_size, patch_size)
    shape_label = (samples_per_img, 1)

    # perform augmentation
    for img_idx, img in enumerate(images):
        img_np_array = np.zeros(shape_img,dtype=dt)
        label_np_array = np.zeros(shape_label,dtype=dt)
        for patch_idx in range(0,samples_per_img):
            # compute current idx
            # save_idx = img_idx * samples_per_img + patch_idx
            save_idx = patch_idx
            # extract patch
            patch = transformation.extract_patch_rotation_scale(images[img_idx], patch_size)
            # normalize patch
            normalized_patch = normalization.std_normalization(patch)
            # save stuff in datastructure
            img_np_array[save_idx, 0, :, :] = normalized_patch
            label_np_array[save_idx,0] = labels[img_idx]
        write.extend_img(dset_img, img_np_array)
        write.extend_labels(dset_label, label_np_array)

    file.close()

    # not a good idea -> too much memory
    # write.write_dataset(name, img_np_array, label_np_array)

    # check the written data -> load dataset and visualize first 1000 images of each class
    loaded_labels = io_h5.load_hdf5_labels(name)
    loaded_images = io_h5.load_hdf5_img(name)

    for label_it in range(0,amount_classes):
        idx = loaded_labels.tolist().index(label_it)
        window_name = 'Label ' + str(label_it)
        img_to_viz = []
        for img_idx in range(0,200):
            img_to_viz.append(loaded_images[idx + img_idx, 0, :, :])

        viz.show_patches(img_to_viz, window_name)

    print 'Finished!'

if __name__ == "__main__":
    main()