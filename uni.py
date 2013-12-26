import sys
import os
import libuni

args = sys.argv

try:
    input_format = args[1]
    output_format = args[2]
    for mediafile in libuni.filterFiles(input_format):
        libuni.Mediafile(mediafile).encode(output_format)
except IndexError:
    print 'uni: usage: uni.py <input> <output>'
    print 'see uni-project.md for more details'
