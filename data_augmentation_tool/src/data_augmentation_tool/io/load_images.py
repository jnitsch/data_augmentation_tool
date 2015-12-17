__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.io.load_images
Functions to load all images from folder.

Given the folder the the functions read in all images found in that folder. Important note: it will sort the folders
alphabetically!!! So the labels will correspond to classes sorted alphabetically A-Z.
"""
import os
import cv2


def read_img_labels(folder):
    """Reads in images which are stored in the folder/classes

    Reads in all images which are stored in following structure
    /folder
    --/class_0
    --/--/img_0
    --/--/img_1
    --/--/...
    --/class_1
    --/--/img_0
    --/--/img_1
    --/...
    The naming of the folders or the images doesn't matter. The images must be stored in a format so that opencv can
    read them via cv2.imread. It sorts the classes alphabetically!

    @param folder The folder which contains the subfolder with different classes.

    @return Returns images as list, and the corresponding labels in seperate list. Third Parameter tells how many different classes were found.
    """
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
                gray = cv2.imread(os.path.join(dir_path, file), cv2.CV_LOAD_IMAGE_GRAYSCALE)

                images.append(gray)
                labels.append(class_index)

            class_index = class_index + 1

    return images, labels, class_index
