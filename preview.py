#!/usr/bin/python3

# Normally the QtGlPreview implementation is recommended as it benefits
# from GPU hardware acceleration.

from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)
preview_config = picam2.preview_configuration()
preview_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam2.configure(preview_config)

picam2.start()
time.sleep(10)
