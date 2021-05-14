from moviepy.editor import *
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from project_consts import *
import os
import time

in_file = 'GOPR1950.MP4'


cmd = "ffmpeg -i {0} -ss 00:00:01.9 -to 00:00:06.95 -async 1 cut.mp4".format(in_file)
print "cmd: ", cmd
os.system(cmd)