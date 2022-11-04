#!/bin/sh
# Launcher.sh

echo `date +"%Y-%M-%d %T"`" - Setting up environment for Green House IoT System. . . " >> /home/pi/logs/Launcher-log.txt

cd /home/pi/MyProjects/AzureIOTHub/RaspberryPiApp

git pull

cd -
