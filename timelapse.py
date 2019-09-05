#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw
#reference: https://picamera.readthedocs.io/en/release-1.12/api_camera.html
 
# for manual dark mode: Set a framerate of 1/3fps, then set shutter
# speed to 3s and ISO to 800, exposure mode to off

from time import sleep
import picamera
from fractions import Fraction
print('done importing!')
WAIT_TIME = 30 # time in seconds
with picamera.PiCamera() as camera:
    # camera.resolution = (820, 616) #crop?
    camera.resolution = (1640, 1232) #2x2 binned
    print('set resoultion to '+str(camera.resolution))
    camera.meter_mode = 'matrix' # 'average' 'spot' 'backlit' 'matrix'
    print('set meter_mode to '+str(camera.meter_mode))
    camera.rotation = 180
    print('set rotation to '+str(camera.rotation))
    camera.drc_strength = 'medium' # 'off' 'low' 'medium' 'high'
    print('set drc_strenght to '+str(camera.drc_strength))
    camera.framerate = Fraction(1, 3)
    print('set framerate to '+str(camera.framerate))
    #camera.shutter_speed = 3000000 #3 seconds
    print('set shutter_speed to '+str(camera.shutter_speed))
    camera.exposure_mode = 'verylong' # 'off' 'auto' 'night' 'nightpreview' 'backlight' 'spotlight' 'sports' 'snow' 'beach' 'verylong' 'fixedfps' 'antishake' 'fireworks'
    print('set exposure_mode to '+str(camera.exposure_mode))
    #camera.iso = 100 # overwrites exposure mode
    print('set iso to '+str(camera.iso))
    camera.awb_mode = 'shade' # 'off' 'auto'  'sunlight'  'cloudy'  'shade'  'tungsten' 'fluorescent'  'incandescent' 'flash' 'horizon'
    print('set awb_mode to '+str(camera.awb_mode))
    print('camera setup done!')
    for filename in camera.capture_continuous('/home/pi/timelapse/output/lapse_{counter:05d}__{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
