#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# uni.py
#
# The [UNI]versal encoder. ;D
#
# (c) 2013-4, Luca J Pears <lucapiras66@gmail.com>

import sys
import os
import libuni

args = sys.argv

try:
    inputformat = args[1]
    outputformat = args[2]
    for mediafile in libuni.filterFiles(inputformat):
        original, converted = libuni.Encoder(mediafile,outputformat).encode()
        print("from:\t{}\nto:\t{}".format(original,converted))
        print()
except IndexError:
    print('uni: usage: uni.py <input> <output>')
    print('see uni-project.md for more details')
