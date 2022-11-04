* How crontab is configured?

$ crontab -e

This will open an editor, there, paste below line:

@reboot python3 /home/pi/MyProjects/AzureIOTHub/RaspberryPiApp/main.py  >/home/pi/logs/cronlog 2>&1

