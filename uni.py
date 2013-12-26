import sys
import json
import os
import libuni

from libuni import die as die
args = sys.argv

def filterfiles(extension, path=os.getcwd()):
    for file_ in os.listdir(path):
        if file_.endswith(extension): yield file_

# Wrapper for print, used in list comprehensions.
def p(what):
    print what

# Initialise the environment, load all the plugins in memory

plugins = []
for plugin in filterfiles('.json','plugins' + os.sep):
    plugins.append(libuni.Plugin(plugin))

if args[1] == 'plugins':    
    print 'Installed plugins:'
    
    for plugin in plugins:
        print '{} (v {}) (by {})'.format(plugin.name,plugin.version,plugin.author)

elif args[1] == 'conversions':
    print 'Possible conversions:'
    
    for plugin in plugins:
        print '{} => {}'.format(plugin.name,','.join(plugin.outputs))

elif (args[1] == 'pretend') or (args[1] == 'convert'):
    try:
        output = args[3]
    except:
        die('not enough arguments.')
    
    for mediafile in filterfiles(args[2]):
        file_ = libuni.Mediafile(mediafile)
        if args[1] == 'pretend':
            [p(f) for f in mediafile.steps(output)]
        else:
            file_.encode(output)

else:
    die('unrecognised command.')
