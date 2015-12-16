__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.augmentation.normalization
Functions to normalize images

Different functions for normalizing images are implemented here
"""

import numpy as np
import cv2

def std_normalization(patch):
    """Normalizes patch

    @param patch Input patch/image which is normalized

    @return The normalized result
    """

    # normalize from 0 to 1
    img = np.divide(patch, 255.0)

    # normalize for mean
    mean, std = cv2.meanStdDev(img)
    img = img - mean

    # normalize for standard dev
    if np.isnan(std).any():
        std = 1.0

    img = np.divide(img, std)

    return img
