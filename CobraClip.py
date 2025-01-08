from pytubeScripts import downloadmp4
from pytubeScripts import downloadmp3

import os
import sys


url = input('Input Video URL\n')

mode = input('MP3? Y/N\n')

#set outputfile location
output_location = ''.join(('C:/Users/', os.getlogin(), '/Downloads/'))

#url = 'https://youtu.be/j_bi5uAigJk'

if mode.upper() == "Y":
    downloadmp3(url, output_location)
else:
    downloadmp4(url, output_location)

# open downloads folder
os.startfile(output_location)
