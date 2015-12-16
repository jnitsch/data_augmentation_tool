__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.utils.visualization
Functions for convently visualizing data.

Contains helper functions to visualize different data
"""

import numpy as np
import cv2
import copy

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


def show_patches(patches, windowname):
    amount_patches = len(patches)
    # contain 20 images per coloum
    img_col = 20
    img_row = amount_patches / img_col + 1
    rows,cols = patches[0].shape[:2]
    print 'Rows: %d Cols: %d' % (rows, cols)
    img = np.empty([(img_row * rows), (img_col * cols)])

    row_idx = 0
    col_idx = 0
    for i, patch in enumerate(patches):
        current_row = row_idx * rows
        current_col = col_idx * cols
        img[current_row:(current_row + rows), current_col:(current_col + cols)] = patch

        # next image should be in next col
        col_idx = col_idx + 1

        # if end of cols reached -> jump in next row and reset cols
        if col_idx % img_col == 0:
            col_idx = 0
            row_idx = row_idx + 1
            #show_single_img_named(patch, 'test')


    # because images were normalized multiply them by 255
    np.multiply(img, 255.0)

    show_single_img_named(img, windowname)