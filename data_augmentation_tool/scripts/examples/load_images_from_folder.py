#!/usr/bin/python

"""
loads img from folder and shows one image of each folder
"""
__author__ = 'Julia Nitsch'
import argparse
import data_augmentation_tool.utils.visualization as util
import data_augmentation_tool.io.load_images as io

def main():
    parser = argparse.ArgumentParser(description='''
    Test to load images and visualize one of each class
    ''')
    parser.add_argument('--folder', help='folder where different classes are stored', default='')
    args = parser.parse_args()
    folder = args.folder

    images, labels, amount_classes = io.read_img_labels(folder)

    for label_it in range(0,amount_classes):
        idx = labels.index(label_it)
        window_name = 'Label ' + str(label_it)
        util.show_single_img_named(images[idx], window_name)

if __name__ == "__main__":
    main()


