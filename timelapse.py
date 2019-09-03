#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep
import picamera
import datetime

Datum = datetime.datetime.now().strftime('%-d.%-m.')
Uhrzeit = datetime.datetime.now().strftime('%H:%M')

WAIT_TIME = 30

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    camera.rotation = 180
    for filename in camera.capture_continuous('/home/pi/timelapse/output/img{timestamp:%H-%M-%S-%f}.jpg'):
        print (Datum, Uhrzeit)
        sleep(WAIT_TIME)
        
