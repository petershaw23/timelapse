#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview(fullscreen=False, window=(100,100,256,192))
    time.sleep(2)
    camera.preview.window=(200,200,256,192)
    time.sleep(2)
    camera.preview.window=(0,0,512,384)
    time.sleep(2)
