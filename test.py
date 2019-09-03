#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import picamera
camera = picamera.PiCamera()
camera.start_preview(alpha=128, fullscreen=False, window=(0, 0, 640, 480))
