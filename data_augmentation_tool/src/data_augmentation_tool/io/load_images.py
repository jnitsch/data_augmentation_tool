__author__ = 'jnitsch'
"""@package data_augmentation_tool.io.load_images
Functions to load all images from folder.

Given the folder the the functions read in all images found in that folder. Important note: it will sort the folders
alphabetically!!! So the labels will correspond to classes sorted alphabetically A-Z.
"""
import os
import cv2

def read_img_labels(folder):
    class_index = 0
    labels = []
    images = []


    #sort it alphabetically to know the order of the labels
    directories = os.listdir(folder)
    directories = sorted(directories)

    for directory_name in directories:
        if os.path.isdir(os.path.join(folder, directory_name)):
            print directory_name
            dir_path = os.path.join(folder, directory_name)

            for file in os.listdir(dir_path):
                print '  ' + file
                img = cv2.imread(os.path.join(dir_path, file))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                images.append(gray)
                labels.append(class_index)

            class_index = class_index + 1

    return images, labels, class_index
