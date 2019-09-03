#!/bin/bash
pwd
# scp timelapse.py hosting126791@188.68.47.235:httpdocs/peter-shaw/timelapse
# this uses rclone, see: https://rclone.org/

rclone sync output/ ftp:httpdocs/peter-shaw/timelapse



