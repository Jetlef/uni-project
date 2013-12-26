import sys
import os
import libuni

args = sys.argv

try:
    inputformat = args[1]
    outputformat = args[2]
    for mediafile in libuni.filterFiles(inputformat):
        print libuni.Encoder(mediafile,outputformat).encode()
except IndexError:
    print 'uni: usage: uni.py <input> <output>'
    print 'see uni-project.md for more details'
