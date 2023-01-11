
from MoistureSensor import MoistureSensor
from PlaySounds import PlaySounds
from DHT11 import DHT11
import time
import asyncio
import time
import board
import RPi.GPIO as GPIO
import dht11
from azure.iot.device import Message
from azure.iot.device import IoTHubDeviceClient
import subprocess
import math

CONNECTION_STRING = "HostName=ih-greenhouse.azure-devices.net;DeviceId=smart-detector-1.0;SharedAccessKey=0Pbb0a+Of7Ii8ApmsxmVdUTe1FNwOO5pi+eXN7bxKrs="

DELAY = 5
TEMPERATURE = 20.0
HUMIDITY = 60
PAYLOAD = '{{"co2Level": "380", "temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}, "lightCount": "1", "lightCapacity": "20", "lightDuration": "8", fanStatus: {fanStatus}, "lightingStatus": "false", "waterpumpStatus": {waterpumpStatus}, "dehumidifierStatus": "false", "cropInfo": {{"cropType": "Fruits", "cropName": "Litchi", "soilphValue": "4.75"}}, "deviceInfo": {{ "deviceId": "smart-detector-1.0", "deviceVersion": "1", "deviceTimestamp": "2022-10-11T12:30:03.4467715Z" }}, "locationInfo": {{ "lat": "18.516726", "lon": "73.856255", "timezone": "Coordinated Universal Time" }}  }}'
# PAYLOAD = '{"co2Level": "380", "temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}, "lightCount": "1", "lightCapacity": "20", "lightDuration": "8", "fanStatus": "false", "lightingStatus": "false", "waterpumpStatus": "false", "dehumidifierStatus": "false", "cropInfo": { "cropType": "Fruits", "cropName": "Litchi", "soilphValue": "4.75" }, "deviceInfo": { "deviceId": "smart-detector-1.0", "deviceVersion": "1", "deviceTimestamp": "2022-10-11T12:30:03.4467715Z" }, "locationInfo": { "lat": "18.516726", "lon": "73.856255", "timezone": "Coordinated Universal Time" } }'
# PAYLOAD = '{"temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}}'
RECEIVED_MESSAGES = 0
KEEP_SPRINKLER_ON = 10
FAN_PIN = 3
SPRINKLER_PIN = 18

dht11 = DHT11()
moistureSensor = MoistureSensor()
playSounds = PlaySounds()

playSounds.play_sound("/home/pi/MyProjects/AzureIOTHub/RaspberryPiApp/Files/welcome.mp3")


def message_handler(message):
    global RECEIVED_MESSAGES
    global KEEP_SPRINKLER_ON
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print("    {}".format(property))

    strMsg = message.data.decode()

    # print(type(strMsg))

    if strMsg == 'MAKE-FAN-ON':
        GPIO.output(FAN_PIN, GPIO.HIGH)
        print('MAKE-FAN-ON')
    elif strMsg == 'MAKE-FAN-OFF':
        GPIO.output(FAN_PIN, GPIO.LOW)
        print('MAKE-FAN-OFF')
    elif strMsg == 'MAKE-SPRINKLER-ON':
        GPIO.output(SPRINKLER_PIN, GPIO.HIGH)
        KEEP_SPRINKLER_ON = 10
        print('MAKE-SPRINKLER-ON')
    elif strMsg == 'MAKE-SPRINKLER-OFF':
        GPIO.output(SPRINKLER_PIN, GPIO.LOW)
        KEEP_SPRINKLER_ON = 10
        print('MAKE-SPRINKLER-OFF')


    print("Total calls received: {}".format(RECEIVED_MESSAGES))


async def main():
    global KEEP_SPRINKLER_ON
    time.sleep(40)

    subprocess.call(
        ['sh', '/home/pi/MyProjects/AzureIOTHub/RaspberryPiApp/Launcher.sh'])

    # GPIO.cleanup()
    # GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SPRINKLER_PIN, GPIO.OUT, initial=GPIO.LOW)
    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(
            CONNECTION_STRING)
        print("Starting the Python IoT Hub C2D Messaging device sample...")

        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:

            try:
                time.sleep(1)
                moisture = math.ceil(moistureSensor.sense_moisture())

                temp_and_humitidy = dht11.get_dht11_sensor_data()
                temp = math.ceil(temp_and_humitidy[0])
                humidity = math.ceil(temp_and_humitidy[1])
                print('temp', temp, 'humidity: ', humidity)
                fileLineVariable = str(temp) + ";" + str(moisture) + ";" + str(humidity)

                with open('/home/pi/MyProjects/AzureIOTHub/RaspberryPiApp/Files/SensorData.txt','w') as f:
                    f.write(fileLineVariable)
                    # f.close() # No need to close I think

                data = PAYLOAD.format(
                    temperature=temp, humidity=humidity, moisture=moisture, fanStatus=GPIO.input(FAN_PIN) , waterpumpStatus=GPIO.input(SPRINKLER_PIN))
                message = Message(data)

                # Get controlled by dashboard sprinkler On/OFF button
                # if number of seconds is not 0.
                # Till this, the lock will not be released
                if KEEP_SPRINKLER_ON > 0:
                    KEEP_SPRINKLER_ON = KEEP_SPRINKLER_ON - 1
                else:
                    if moisture < 20:
                        GPIO.output(SPRINKLER_PIN, GPIO.HIGH)
                    else:
                        GPIO.output(SPRINKLER_PIN, GPIO.LOW)


                # Send a message to the IoT hub
                print(f"Sending message: {message}")
                await client.send_message(message)
                print("Message successfully sent")

            except Exception as error:

                time.sleep(2.0)
                print(error)
                continue

    except Exception as error:
        print(error.args[0])
        # close the file
        # f.close()
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()


if __name__ == '__main__':

    try:
        asyncio.run(main())
    except Exception as error:
        print("Exception in main" + error.args[0])

        print("Cleaning up GPIO ..")
        GPIO.cleanup()

    print("Cleaning up GPIO ..")
    GPIO.cleanup()
