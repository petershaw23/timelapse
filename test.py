
#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw DARK MODE

#exposure modes:

  #  'off'
  #  'auto'
  #  'night'
  #  'nightpreview'
  #  'backlight'
  #  'spotlight'
  #  'sports'
  #  'snow'
  #  'beach'
  #  'verylong'
  #  'fixedfps'
  #  'antishake'
  #  'fireworks'



import picamera
from time import sleep
from fractions import Fraction

WAIT_TIME = 30 # time in seconds

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    camera.meter_mode = 'matrix'
    camera.rotation = 180
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    camera.framerate = Fraction(1, 6)
    camera.exposure_mode = 'night'
    # camera.iso = 800
    camera.awb_mode = 'shade'   # 'off' 'auto'  'sunlight'  'cloudy'  'shade'  'tungsten' 'fluorescent'  'incandescent' 'flash' 'horizon'

    for filename in camera.capture_continuous('/home/pi/timelapse/output/night_{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
