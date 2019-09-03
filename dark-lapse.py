
#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw DARK MODE

import picamera
from time import sleep
from fractions import Fraction

WAIT_TIME = 30 # time in seconds

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = 6000000
    camera.exposure_mode = 'off'
    camera.iso = 800
    # Give the camera a good long time to measure AWB
    # (you may wish to use fixed AWB instead)
    sleep(10)
    # Finally, capture an image with a 6s exposure. Due
    # to mode switching on the still port, this will take
    # longer than 6 seconds
    for filename in camera.capture_continuous('/home/pi/timelapse/output/dark_{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
