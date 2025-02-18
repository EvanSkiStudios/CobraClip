from pytubeScripts import *

import os
import sys

mode = ''

argsLen = len(sys.argv)
if argsLen > 1:
    url = sys.argv[1]
    if argsLen > 2:
        mode = sys.argv[2]
else:
    url = input('Input Video URL\n')

# set outputfile location
output_location = ''.join(('C:/Users/', os.getlogin(), '/Downloads/'))

# url = 'https://youtu.be/j_bi5uAigJk'
if mode.upper() == "-audio":
    downloadAudio(url, output_location)
else:
    downloadmp4(url, output_location)

# open downloads folder
os.startfile(output_location)
