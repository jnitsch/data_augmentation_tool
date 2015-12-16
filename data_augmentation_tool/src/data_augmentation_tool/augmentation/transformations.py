__author__ = 'Julia Nitsch'
"""@package data_augmentation_tool.augmentation.normalization
Functions to manipulate image and extract patches

Different functions for extracting patches and manipulation of the data
"""

import cv2
from random import randint
import data_augmentation_tool.utils.visualization as viz


def extract_patch(img, patchsize):
    """Extracts random patch from imag

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """

    height, width = img.shape[:2]

    # check if image is larger as patchsize
    if height <= patchsize or width <= patchsize:
        # upscale img to patchsize and return it
        patch = cv2.resize(img, (patchsize, patchsize))
        return patch

    # image is large enough to be sampled
    sz = int(patchsize /2)
    width_limit = width - sz - 1
    height_limit = height - sz -1

    midpoint_x = width / 2
    midpoint_y = height /2

    if (sz + 1) < width_limit and (sz + 1) < height_limit:
        # img large enough to sample in the middle
        midpoint_x = randint(sz + 1, width_limit)
        midpoint_y = randint(sz + 1, height_limit)

    patch = img[(int(midpoint_y) - sz) : (int(midpoint_y) + sz + 1), (int(midpoint_x) - sz) : (int(midpoint_x) + sz + 1)]
    return patch


def extract_patch_fliplr(img, patchsize):
    """Extracts random patch from image and rotate it by randomly by 0, 90,180 or 270 degree

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """

    # extract patch
    patch = extract_patch(img, patchsize)
    rows,cols = patch.shape

    # rotate random by multiple of 90 degree
    rot = randint(0,4) * 90
    M = cv2.getRotationMatrix2D((cols/2,rows/2),rot,1)
    dst = cv2.warpAffine(patch,M,(cols, rows),flags=cv2.WARP_INVERSE_MAP,borderMode=cv2.BORDER_REPLICATE)
    return dst


def extract_patch_rotation(img, patchsize):
    """Extracts random patch from randomly rotated image

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """
    # rotate whole image randomly
    rot = randint(0,359)
    rows,cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),rot,1)
    rotated_img = cv2.warpAffine(img,M,(cols, rows),flags=cv2.WARP_INVERSE_MAP,borderMode=cv2.BORDER_REPLICATE)
    # extract patch from rotated image
    patch = extract_patch(rotated_img, patchsize)

    # return extracted patch
    return patch


def extract_patch_rotation_scale(img, patchsize):
    """Scales given image randomly between 90% and 110% of its orig, rotates it randomly and extracts patch of given
    size.

    @param img Input image where patch should be selected
    @param patchsize Size of patch (width  = height = patchsize)

    @return The extracted patch
    """
    height, width = img.shape[:2]

    # determine scale factor
    scale = float(randint(90,110)) / 100.0

    # resize img
    resized_height = int(height * scale)
    resized_width = int(width * scale)
    resized_img = cv2.resize(img, (resized_height, resized_width))

    # extract image of rotated img
    patch = extract_patch_rotation(resized_img, patchsize)

    # return patch
    return patch
