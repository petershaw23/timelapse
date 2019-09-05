#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw
#reference: https://picamera.readthedocs.io/en/release-1.12/api_camera.html

from time import sleep
import picamera
from fractions import Fraction
print('done importing!')
WAIT_TIME = 30 # time in seconds
with picamera.PiCamera() as camera:
    # camera.resolution = (820, 616) #crop?
    camera.resolution = (1640, 1232) #2x2 binned
    camera.meter_mode = 'matrix' # 'average' 'spot' 'backlit' 'matrix'
    camera.rotation = 180
    camera.drc_strength = 'medium' # 'off' 'low' 'medium' 'high'
    
    # for dark mode: Set a framerate of 1/3fps, then set shutter
    # speed to 3s and ISO to 800, exposure mode to off
    
    camera.framerate = Fraction(1, 3)
    #camera.shutter_speed = 3000000 #3 seconds
    camera.exposure_mode = 'verylong' # 'off' 'auto' 'night' 'nightpreview' 'backlight' 'spotlight' 'sports' 'snow' 'beach' 'verylong' 'fixedfps' 'antishake' 'fireworks'
    #camera.iso = 100 # overwrites exposure mode
    camera.awb_mode = 'shade' # 'off' 'auto'  'sunlight'  'cloudy'  'shade'  'tungsten' 'fluorescent'  'incandescent' 'flash' 'horizon'
    print('init cam done!')
    for filename in camera.capture_continuous('/home/pi/timelapse/output/lapse_{counter:05d}__{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
