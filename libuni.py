# libuni.py
#
# Support library for uni.py
#
# (c) 2013-4, Luca J Pears <lucapiras66@gmail.com>

import json
import sys
import urllib
import os

def die(why):
    print 'UNI -- error: ' + why + ' Type "cat help" for more help.'
    sys.exit()

def justdie(): sys.exit()

def qget(url):
    return urllib.urlopen(url).read()

def qwrite(where,what):
    with open(where,'w') as where:
        where.write(what)

class Plugin():
    
    def __init__(self, plugin):
        plugin = 'plugins' + os.sep + plugin
        self.contents = json.load(open(plugin))
        try:
            self.contents = json.load(open(plugin))
        except IOError:
            print 'Plugin "{}" not found.'.format(plugin)
            justdie()
        
        try:
            self.name = self.contents['name']
            self.author = self.contents['author']
            self.version = self.contents['version']
            self.encoders = self.contents['outputs']
            self.outputs = self.encoders.keys()
        except KeyError:
            print 'Plugin "{}" is corrupt/invalid. Retry with a clean copy.'.format(plugin)
            justdie()
        
    def convertTo(self, output):
        try:
            return self.encoders[output]
        except KeyError:
            print 'Conversion "{}" => "{}" not implemented.'.format(self.name,output)
            justdie()

class Mediafile():
    
    def __init__(self, mediafile):
        self.mediafile = mediafile
        
        # Split <file_name> in two parts: the extensionless <file_name>, and its extension.
        p = mediafile.rfind('.') + 1
        self.name, self.extension = mediafile[:p-1], mediafile[p:]
        
        # Find the appropriate plugin.
        self.plugin = Plugin(self.extension + '.json')
    
    def steps(self, output):
        for instruction in self.plugin.convertTo(output):
            yield instruction.replace('<file>',self.name).replace('|','"')
    
    def encode(self, output):
        [os.system(step) for step in self.steps(output)]
