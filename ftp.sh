#!/bin/bash
pwd
#scp timelapse.py hosting126791@188.68.47.235:httpdocs/peter-shaw/timelapse
rsync -avz output/ hosting126791@188.68.47.235:httpdocs/peter-shaw/timelapse
