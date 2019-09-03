#!/usr/bin/python
# -*- coding:utf-8 -*-
#timelapse script by psw
from time import sleep
import picamera
import datetime

Datum = datetime.datetime.now().strftime('%-d.%-m.')
Uhrzeit = datetime.datetime.now().strftime('%H:%M:%S')

WAIT_TIME = 30

with picamera.PiCamera() as camera:
    camera.resolution = (820, 616)
    camera.start_preview()
    camera.meter_mode = 'matrix'
    camera.rotation = 180
    sleep(2)
    for filename in camera.capture_continuous('/home/pi/timelapse/output/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print (Datum, Uhrzeit)
        camera.stop_preview()
        sleep(WAIT_TIME)
        
