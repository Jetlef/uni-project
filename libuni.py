#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# libuni.py
#
# Support library for uni.py
#
# (c) 2013-4, Luca J Pears <lucapiras66@gmail.com>

import json
import sys
import urllib
import os

class PluginNotFoundError(Exception): pass

class ConversionNotSupportedError(Exception): pass

def filterFiles(extension, path=os.getcwd()):
    for file_ in os.listdir(path):
        if file_.endswith(extension): yield file_

class Encoder():
    
    def __init__(self, inputfile, outputformat):
        self.inputfile = inputfile
        self.outputformat = outputformat
        self.barename, extension = inputfile.rsplit('.',1)
        
        try:
            pluginpath = 'plugins' + os.sep + extension + '.json'
            plugin = json.load(open(pluginpath))
        except IOError:
            raise PluginNotFoundError(pluginpath)
        
        try:
            self.steps = []
            for step in plugin['outputs'][outputformat]:
                step = step.replace('<file>',self.barename)
                step = step.replace('|','"')
                step = step.replace('#',os.sep)
                program = step.split()[0]
                if not os.path.isfile(program):
                    raise PluginNotFoundError(program)
                
                self.steps.append(step)
        except KeyError:
            message = '{} to {}'.format(extension,outputformat)
            raise ConversionNotSupportedError(message)

    def encode(self):
        [os.system(step) for step in self.steps]
        return self.inputfile, '{}.{}'.format(self.barename,self.outputformat)
