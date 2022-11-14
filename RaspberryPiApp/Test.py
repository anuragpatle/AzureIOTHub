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

# from playsound import playsound

# It is a text value that we want to convert to audio
text_val = 'Welcome! The device is getting ready.'

# Here are converting in English Language
language = 'en'

# Passing the text and language to the engine,
# here we have assign slow=False. Which denotes
# the module that the transformed audio should
# have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)

#Here we are saving the transformed audio in a mp3 file named
# exam.mp3
obj.save("./Files/welcome.mp3")

# Play the exam.mp3 file
# playsound("./Files/lights_turned_on.mp3") # if this line gives you error then: pip install playsound==1.2.2


########################################## Test Play sounds ###################################################
# from pygame import mixer, time

#Instantiate mixer
# mixer.init()

#Load audio file
# mixer.music.load('./Files/lights_turned_on.mp3')

# print("music started playing....")

#Set preferred volume
# mixer.music.set_volume(1)

#Play the music
# mixer.music.play()

#Infinite loop
# while True:
# 	print("------------------------------------------------------------------------------------")
# 	print("Press 'p' to pause the music")
# 	print("Press 'r' to resume the music")
# 	print("Press 'e' to exit the program")

# 	#take user input
# 	userInput = input(" ")

# 	if userInput == 'p':

# 		# Pause the music
# 		mixer.music.pause()
# 		print("music is paused....")
# 	elif userInput == 'r':

# 		# Resume the music
# 		mixer.music.unpause()
# 		print("music is resumed....")
# 	elif userInput == 'e':

# 		# Stop the music playback
# 		mixer.music.stop()
# 		print("music is stopped....")
# 		break

# Use above while loop or use below while loop
# while mixer.music.get_busy():
#     time.Clock().tick(10)


########################################################### Over writing file data to SensorData.txt ##################
# # opening the file in write only mode
# f = open("./Files/SensorData.txt", "w")
# # f is the File Handler
# f.write("25;23;55")
# # close the file
# f.close()
