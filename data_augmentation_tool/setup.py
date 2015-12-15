#!/usr/bin/env python

from distutils.core import setup

setup(name='data_augmentation_tool',
      version='0.0',
      description='Tool for loading images, augment them and save them in a format so that caffe can read it',
      author='Julia Nitsch',
      author_email='julia.nitsch@gmail.com',
      license='BSD',
      packages=['data_augmentation_tool',
                'data_augmentation_tool.io',
                'data_augmentation_tool.augmentation',
                'data_augmentation_tool.utils',],
      package_dir={'': 'src'},
      scripts=['scripts/examples/load_hdf5_file.py'],
      install_requires=['hdf5'],
      zip_safe=False)


