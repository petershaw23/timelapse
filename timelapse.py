#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep
import picamera

WAIT_TIME = 30

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    camera.rotation = 180
    print ('go')
    for filename in camera.capture_continuous('/home/pi/timelapse/output/img{timestamp:%H-%M-%S-%f}.jpg'):
        sleep(WAIT_TIME)
        print ('pic')
