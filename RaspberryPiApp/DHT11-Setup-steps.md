In this tutorial we use a DHT11 temperature & humidity sensor. With a Python script running on your Raspberry Pi, we will read the ambient temperature and humidity. When you have completed this tutorial, you will be able to connect the DHT11 sensor to your Pi via the GPIO pins. You’ll also have the basic code to convert the output signal of the sensor to useable information in your Python script. This tutorial can also be used for a DHT22 sensor.

Prepare your Pi
First, you need to have a Raspberry Pi running on the latest version of Raspberry Pi OS. This version includes “Thonny”. We’ll use this user-friendly IDE to write our Python code. If you’re not familiar with Python or with Thonny or GPIO-pins, I suggest to have a look at our tutorials “How to write your first Python program on the Raspberry Pi” and/or “How to use the Raspberry Pi GPIO pins” to have a quick introduction.

Prepare the extra hardware
Next, you’ll need some extra hardware:

a breadboard (we are using a 400 points breadboard)
an DHT11 or DHT22 temperature and humidity sensor (we are using the DHT11 sensor)
Dupont jumper wires
a T-cobbler (optional)
a 40 pin GPIO cable (optional)
If you miss any hardware, don’t hesitate to visit our shop. We have a nice kit which contains all the things you need tot start.Raspberry Pi GPIO kit

Get to know the DHT11 temperature and humidity sensor
DHT11 temperature and humidity sensor
The DHT11 is a low-cost and popular sensor for measuring temperature and humidity. The device on the module requires 3 connections to the Raspberry Pi : 3,3V ; GND and a GPIO input pin. As the output signal is 3,3V , it can be directly connected to a GPIO input pin of the Raspberry Pi. The temperature range is 0-50°C (+/-2°C) and the humidity range is 20-90% (+/-5%). The sensor is quite slow and has limited accuracy, but it is an ideal device for your experiments.

Set up the hardware part
Be careful ! Before starting to connect wires on the GPIO pins of your Raspberry Pi, make sure you properly shut down the Pi and removed the power cable from the board!

raspberry pi DHT11 temperature and humidity sensor
connect the 40 pin cable on the GPIO pins of your Pi (if necessary, remove the cover of your Pi first)
plug the cobbler onto the breadboard as shown in the figure above or below
plug the other end of the 40 pin cable in the T-cobbler
connect the VCC pin of the sensor to the 3,3V pin (red wire)
connect the OUTPUT pin of the sensor to pin 23 (yellow wire)
connect the GND of the sensor to a GPIO GND pin (black cable)
Raspberry Pi DHT11 temperature and humidity sensor
Install the Python libraries
The DHT11 sensor communicates with a specific protocol. Fortunately, we don’t have to deal with these details and thanks to Adafruit, we can use Python libraries to retrieve the measurements easily. To download the libraries, make sure your Pi has access to the internet. It takes some time to complete the installation of these libraries. But be patient, at this time and for so far we are aware, it is the easiest way to let your Pi get the measurements of the DHT11-sensor.

Prepare the installation of CircuitPython libraries
To be able to easily communicate with some sensors, CircuitPython has been developed. So, before installing the specific DHT-library, we have to do some preparation work.

Open a terminal window and write following commands:

In our case, it is really important to use the latest version of Raspberry Pi OS ! Even if it takes some time, do not skip the next step !

sudo apt update
sudo apt full-upgrade
sudo apt install python3-pip
sudo pip3 install --upgrade setuptools
sudo reboot
Then install and run a script developed by Adafruit :

sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
The script will probably ask you to update your python version to Version 3. Choose : y

Raspberry Pi update CircuitPython
At the end of the process, you will be asked to reboot. Choose : y

After the reboot, we are ready to install the DHT-library. If you are having any issues, have a look at “Installing CircuitPython Libraries on Raspberry Pi“. This Adafruit webpage has more explanations.

Install the CircuitPython-DHT Library
Open a terminal window and write following commands:

pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
That’s it, the necessary libraries should be installed now. If you need more information, visit “Installing the CircuitPython-DHT Library“.

Write the code
The aim is to write a very simple Python program that allows us to visualize the measured ambient temperature and humidity. To write the code, we use the Thonny IDE. You can find Thonny under the application menu of your Raspberry Pi.

Write or paste following code in the IDE:

import time
import board
import adafruit_dht
import psutil
# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)
Some explanations about the code:

import board this library will be used to define with which GPIO pin we connected the DHT11 sensor.
import adafruit_dht DHT-sensor specific library.
import psutil library for retrieving information on the running processes.
Be careful, Python is whitespace-sensitive. Don’t remove the “tab” before the code line after the for, if, … commands !
After the import-section, we have to write some code to avoid that our script blocks after the first run. Indeed, after we fisrt ran the script with Thonny, some sensor-processes keep running in the background. And if we want to run our script again, the script will block and render an error message. To avoid this, we use a workaround. So, we first check if the sensor related processes are running. If this is the case, we kill them. By the way, we don’t need that workaround if we launch our Python script from the terminal window.
sensor = adafruit_dht.DHT11(board.D23) Here we define the type of sensor and pin number. Change to DHT22 if you use this type of DHT-sensor. And change the pin number if you are using another pin.
temp = sensor.temperaturereading the temperature value from the sensor.
humidity = sensor.humidityreading the humidity value from the sensor.
print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity)) printing the results on the screen. Considering the limited accuracy of the sensor, the results are formatted with no decimals.
DHT-sensors are hard to read for Linux-based operating systems. That’s why reading errors happen quite often (see the example just below). After printing the type of error, we keep going with the next reading.
time.sleep(2.0): wait for 2 seconds.
