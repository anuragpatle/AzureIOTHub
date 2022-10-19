import asyncio
import time
import board
import RPi.GPIO as GPIO

DELAY = 5
TEMPERATURE = 20.0
HUMIDITY = 60
PAYLOAD = '{{"temperature": {temperature}, "humidity": {humidity}, "moisture": {moisture}}}'

FAN_PIN = 24
SPRINKLER_PIN = 25
moisture = "false"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(26, GPIO.OUT)
