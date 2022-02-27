"""
Run this file to activate the fridge guard
"""
from camerasystem import finish_recording, start_recording
from test_gpio import is_stealing
from postprocess import process_video

import time, signal

FILENAMES = []


class GracefulExit:
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        signal.signal(signal.SIGQUIT, self.exit_gracefully)

    def __bool__(self):
        return self.kill_now

    def exit_gracefully(self, *args):
        self.kill_now = True


should_exit = GracefulExit()
while not should_exit:
    if is_stealing():
        filename = start_recording()
        time.sleep(5)
        finish_recording()
        FILENAMES.append(filename)

for filename in FILENAMES:
    print("Processing", filename)
    if process_video(filename):
        print("Found potential thief taking from fridge!!!")
    else:
        print("No faces found")
