"""
Run this file to activate the fridge guard
"""
from camerasystem import finish_recording, start_recording
from test_gpio import is_stealing
from postprocess import process_video
import time


while True:
    if is_stealing():
        start_recording()
        time.sleep(5)
        fname = finish_recording()
        print("Analysing Footage...")
        if process_video(fname):
            print("Found potential thief taking from fridge!!!")
        else:
            print("No faces found")
        
            