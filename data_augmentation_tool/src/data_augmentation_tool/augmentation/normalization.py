__author__ = 'jnitsch'
"""@package data_augmentation_tool.augmentation.normalization
Functions to normalize images

Different functions for normalizing images are implemented here
"""

import numpy as np


def std_normalization(patch):
    """Normalizes patch

    @param patch Input patch/image which is normalized

    @return The normalized result
    """

    # normalize from 0 to 1
    img = np.divide(patch, 255)

    # normalize for mean
    img = img - np.mean(img)

    # normalize for standard dev
    img = np.divide(img, np.std(img))

    return img
