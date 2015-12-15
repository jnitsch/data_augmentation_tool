__author__ = 'jnitsch'
"""@package data_augmentation_tool.augmentation.normalization
Functions to manipulate image and extract patches

Different functions for extracting patches and manipulation of the data
"""

import cv2
from random import randint



def extract_patch(img, patchsize):
    """Extracts random patch from imag

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """
    height, width = img.shape[:2]

    sz = int(patchsize /2)
    midpoint_x = randint(sz + 1, width - sz - 1)
    midpoint_y = randint(sz + 1, height - sz -1)

    patch = img[(midpoint_y - sz) : (midpoint_y + sz + 1), (midpoint_x - sz) : (midpoint_x + sz + 1)]
    return patch


def extract_patch_fliplr(img, patchsize):
    """Extracts random patch from image and rotate it by randomly by 0, 90,180 or 270 degree

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """

    #extract patch
    patch = extract_patch(img, patchsize)
    rows,cols = patch.shape

    # rotate random by multiple of 90 degree
    rot = randint(0,4) * 90
    M = cv2.getRotationMatrix2D((cols/2,rows/2),rot,1)
    dst = cv2.warpAffine(patch,M,(cols, rows),flags=cv2.WARP_INVERSE_MAP,borderMode=cv2.BORDER_REPLICATE)
    return dst