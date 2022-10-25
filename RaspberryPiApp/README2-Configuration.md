HostName=ih-greenhouse.azure-devices.net;DeviceId=RaspberryPI-1;SharedAccessKey=4EbDwtR+WfC2Qn+sFeDoqzTQ8crPNkMI+MPJCgOrrkA=

HostName=ih-greenhouse.azure-devices.net;DeviceId=RaspberryPI-1;SharedAccessKey=Oj9z/DjShgsHsOI4Z5nC1xmBNYop81nB3LIgRe9XJKk=

4EbDwtR+WfC2Qn+sFeDoqzTQ8crPNkMI+MPJCgOrrkA=

Oj9z/DjShgsHsOI4Z5nC1xmBNYop81nB3LIgRe9XJKk=
RaspberryPI-1

Github token: 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

1.  Install azure extension
- Go to cloud shell on azure portal (top bar)
- az extension add --source https://github.com/Azure/azure-iot-cli-extension/releases/download/v0.17.3/azure_iot-0.17.3-py3-none-any.whl

2. How to start this app
- node index.js 'HostName=ih-greenhouse.azure-devices.net;DeviceId=RaspberryPI-1;SharedAccessKey=4EbDwtR+WfC2Qn+sFeDoqzTQ8crPNkMI+MPJCgOrrkA='

3. Creating Virtual Env
- $ pip3 install virtualenv
- $ virtualenv venv_greenhouse # a folder with name 'venv_greenhouse' will get created.
- $ source /home/zf/Documents/MyProjects/Python_Virtual_Env/venv_greenhouse/bin/activate
- (venv_greenhouse) root@raspberrypi:/home/zf/Documents/MyProjects/Python_Virtual_Env/venv_greenhouse/bin#



4. Setting up dht 11 using IOT hub azure

Reffered:
https://social.technet.microsoft.com/wiki/contents/articles/54368.azure-cloud-services-for-raspberry-pi-4-how-to-send-sensor-data-to-azure-iot-hub.aspx


- BCM Pin 17 as the communication channel between Raspberry Pi and DHT 11

5. Setting Soil Moisture Sensor
- VCC -> 5V, GND -> GND, SIG -> GPIO 21


6. DHT 11 Setup, Method 2

    Prepare the installation of CircuitPython libraries
    To be able to easily communicate with some sensors, CircuitPython has been developed. So, before installing the specific DHT-library, we have to do some preparation work.

    Open a terminal window and write following commands:

    In our case, it is really important to use the latest version of Raspberry Pi OS ! Even if it takes some time, do not skip the next step !

    sudo apt updateHi
    sudo apt full-upgrade
    sudo apt install python3-pip
    sudo pip3 install --upgrade setuptools
    sudo reboot
    Then install and run a script developed by Adafruit :

    sudo pip3 install --upgrade adafruit-python-shell
    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    sudo python3 raspi-blinka.py


7. Pins Details:

1. If temperature goes above 25`C, Led GPIO2 OR PIN3 will turn ON
2.

