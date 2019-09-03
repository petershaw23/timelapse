#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw
from time import sleep
import picamera

WAIT_TIME = 30 # time in seconds

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    camera.meter_mode = 'matrix'
    camera.rotation = 180
    sleep(2)
    for filename in camera.capture_continuous('/home/pi/timelapse/output/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        sleep(WAIT_TIME)
