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
    if random.randint(0, 5) < 3:
        return False
    else:
        return True


PICAM2 = Picamera2()
video_config = PICAM2.video_configuration()
video_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
video_config["controls"]["NoiseReductionMode"] = 0
PICAM2.configure(video_config)

PREVIEW = NullPreview(PICAM2)
ENCODER = H264Encoder(10000000)

CURRENT_FILENAME = ""

def start_recording():
    assert CURRENT_FNAME == ""
    timestamp = time.strftime('%b-%d-%Y_%H%M', time.localtime())
    fname = "Recordings/" + timestamp + ".h264"
    ENCODER.output = open(fname, 'wb')
    PICAM2.encoder = ENCODER
    PICAM2.start_encoder()
    PICAM2.start()
    CURRENT_FNAME = fname
    return fname


def finish_recording():
    assert CURRENT_FILENAME != ""
    PICAM2.stop()
    PICAM2.stop_encoder()
    fname, CURRENT_FILENAME = CURRENT_FILENAME, ""
    return fname
        
"""
light_on = True
while light_on:
    time.sleep(2)
    light_on = is_light_on()
    """