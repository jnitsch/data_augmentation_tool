__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.utils.visualization
Functions for convently visualizing data.

Contains helper functions to visualize different data
"""

import numpy as np
import cv2


def show_single_img(img):
    """Shows img with opencv window name 'Single Image'. Waits blocking until user presses any key.

    @param img The image which is shown.
    """
    window_name = 'Single Image'
    show_single_img_named(img, window_name)


def show_single_img_named(img, window_name):
    """Shows img with opencv. Waits blocking until user presses any key.

    @param img The image which is shown.
    @param window_name The name of the opencv window which displays the img
    """
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyWindow(window_name)