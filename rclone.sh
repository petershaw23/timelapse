#!/bin/bash
# scp timelapse.py hosting126791@188.68.47.235:httpdocs/peter-shaw/timelapse
# this uses rclone, see: https://rclone.org/ needs to setup via "rclone config" first.
source /home/pi/.profile
rclone sync -P output/ ftp:httpdocs/peter-shaw/timelapse



