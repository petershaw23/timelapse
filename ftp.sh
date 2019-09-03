#!/bin/bash
pwd
# scp timelapse.py hosting126791@188.68.47.235:httpdocs/peter-shaw/timelapse
# rclone script


progName=$(basename -- "$0")
echo "$progName ver 1.5  written by Claude Pageau"

# Customize rclone sync variables Below
# ---------------------------------------
rcloneName="ftp"
syncRoot="/home/pi/timelapse"
localSyncDir="output"
remoteSyncDir="httpdocs/peter-shaw/timelapse"
# ---------------------------------------

# Display Users Settings
echo "----------- SETTINGS -------------
rcloneName   : $rcloneName
syncRoot     : $syncRoot
localSyncDir : $localSyncDir
remoteSyncDir: $remoteSyncDir
---------------------------------"
if pidof -o %PPID -x "$progName"; then
    echo "WARN  - $progName Already Running. Only One Allowed."
else
    if [ -f /usr/bin/rclone ]; then
        rclone -V   # Display rclone version
        if [ ! -d "$localSyncDir" ] ; then
           echo "---------------------------------------------------"
           echo "ERROR - localSyncDir=$localSyncDir Does Not Exist."
           echo "        Please Investigate Bye ..."
           exit 1
        fi

        /usr/bin/rclone listremotes | grep "$rcloneName"
        if [ $? == 0 ]; then
           echo "/usr/bin/rclone sync -v $localSyncDir $rcloneName:$remoteSyncDir"
           echo "One Moment Please ..."
           /usr/bin/rclone sync -v $localSyncDir $rcloneName:$remoteSyncDir
           if [ ! $? -eq 0 ]; then
               echo "---------------------------------------------------"
               echo "ERROR - rclone sync failed. Review output for Possible Cause"
           else
               echo "INFO  - Sync Successful ..."
           fi
        else
           echo "---------------------------------------------------"
           echo "ERROR - remoteName $rcloneName Does not Exist"
           echo "List of Remote Names"
           echo "-------------------"
           rclone listremotes

