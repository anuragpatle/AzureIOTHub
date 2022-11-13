import asyncio
import time



################################################### LED TEST #################################################
# import board
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# ledPin = 2
# GPIO.setup(ledPin, GPIO.OUT)


# for i in range(50):
# 	print("LED turning on.")
# 	GPIO.output(ledPin, GPIO.HIGH)
# 	time.sleep(0.5)
# 	print("LED turning off.")
# 	GPIO.output(ledPin, GPIO.LOW)
# 	time.sleep(0.5)


################################################## Speech Test ######################################################

# Import the gTTS module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio

from playsound import playsound

# It is a text value that we want to convert to audio
text_val = 'Lights Turned OFF!'

# Here are converting in English Language
language = 'en'

# Passing the text and language to the engine,
# here we have assign slow=False. Which denotes
# the module that the transformed audio should
# have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)

#Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("./Files/lights_turned_on.mp3")

# Play the exam.mp3 file
playsound("./Files/lights_turned_off.mp3") # if this line gives you error then: pip install playsound==1.2.2
