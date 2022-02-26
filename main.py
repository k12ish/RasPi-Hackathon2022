"""
Run this file to activate the fridge guard
"""
from camerasystem import finish_recording, start_recording
import time

while True:
    if accelorometer:
        start_recording()
        time.sleep(60)
        finish_recording()
    time.sleep(5)