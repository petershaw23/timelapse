#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw
from time import sleep
import picamera
from fractions import Fraction

WAIT_TIME = 30 # time in seconds
with picamera.PiCamera() as camera:
    # camera.resolution = (820, 616) #crop?
    camera.resolution = (1640, 1232) #2x2 binned
    camera.meter_mode = 'matrix' # 'average' 'spot' 'backlit' 'matrix'
    camera.rotation = 180
    # camera.drc_strength = 'high' # 'off' 'low' 'medium' 'high'
    
    # for dark mode: Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800, exposure mode to off
    
    camera.framerate = Fraction(1, 6)
    # camera.shutter_speed = 6000000 #6 seconds
    camera.exposure_mode = 'night' # 'off' 'auto' 'night' 'nightpreview' 'backlight' 'spotlight' 'sports' 'snow' 'beach' 'verylong' 'fixedfps' 'antishake' 'fireworks'
    # camera.iso = 800 # overwrites exposure mode
    camera.awb_mode = 'shade' # 'off' 'auto'  'sunlight'  'cloudy'  'shade'  'tungsten' 'fluorescent'  'incandescent' 'flash' 'horizon'
    
    for filename in camera.capture_continuous('/home/pi/timelapse/output/lapse_{counter:05d}__{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print(camera.shutter_speed, camera.iso)
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
