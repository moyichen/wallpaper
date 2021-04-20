#!/bin/sh

CURPATH=$(cd "$(dirname "$0")"; pwd)
cd $CURPATH
echo $CURPATH

cp -f ./com.wallpaper.plist ~/Library/LaunchAgents/com.wallpaper.plist

cd ~/Library/LaunchAgents
pwd

launchctl unload -w com.wallpaper.plist
launchctl load -w com.wallpaper.plist
