"""
This module records video from a Rasberry Pi
"""

from null_preview import *
from h264_encoder import *
from picamera2 import *
from qt_gl_preview import *
import time, os, fnmatch, shutil
import random

def is_light_on():
    time.sleep(5)
    if random.randint(0, 5) < 3:
        return False
    else:
        return True


t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
docu = ("real-time documentary - " + timestamp + ".h264")

picam2 = Picamera2()
video_config = picam2.video_configuration()
video_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
video_config["controls"]["NoiseReductionMode"] = 0
picam2.configure(video_config)

preview = NullPreview(picam2)
encoder = H264Encoder(10000000)

encoder.output = open(docu, 'wb')
picam2.encoder = encoder
picam2.start_encoder()
picam2.start()
time.sleep(2)
#size = picam2.sensor_resolution

time.sleep(2)
"""
light_on = True
while light_on:
    time.sleep(2)
    light_on = is_light_on()
    """
picam2.stop()
picam2.stop_encoder()
    
    