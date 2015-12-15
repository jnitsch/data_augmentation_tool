__author__ = 'jnitsch'
"""@package data_augmentation_tool.utils.visualization
Functions for convently visualizing data.

Contains helper functions to visualize different data
"""

import numpy as np
import cv2


def show_single_img(img):
    window_name = 'Single Image'
    show_single_img_named(img, window_name)


def show_single_img_named(img, window_name):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)