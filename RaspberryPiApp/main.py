from MoistureSensor import MoistureSensor
from DHT11 import DHT11
import time
import asyncio
import time
import board
import RPi.GPIO as GPIO
import dht11
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient

CONNECTION_STRING="HostName=ih-greenhouse.azure-devices.net;DeviceId=smart-detector-1.0;SharedAccessKey=0Pbb0a+Of7Ii8ApmsxmVdUTe1FNwOO5pi+eXN7bxKrs="

DELAY = 5
TEMPERATURE = 20.0
HUMIDITY = 60
PAYLOAD = '{{"co2Level": "380", "temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}, "lightCount": "1", "lightCapacity": "20", "lightDuration": "8", "fanStatus": "false", "lightingStatus": "false", "waterpumpStatus": "false", "dehumidifierStatus": "false", "cropInfo": {{"cropType": "Fruits", "cropName": "Litchi", "soilphValue": "4.75"}}, "deviceInfo": {{ "deviceId": "smart-detector-1.0", "deviceVersion": "1", "deviceTimestamp": "2022-10-11T12:30:03.4467715Z" }}, "locationInfo": {{ "lat": "18.516726", "lon": "73.856255", "timezone": "Coordinated Universal Time" }}  }}'
# PAYLOAD = '{"co2Level": "380", "temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}, "lightCount": "1", "lightCapacity": "20", "lightDuration": "8", "fanStatus": "false", "lightingStatus": "false", "waterpumpStatus": "false", "dehumidifierStatus": "false", "cropInfo": { "cropType": "Fruits", "cropName": "Litchi", "soilphValue": "4.75" }, "deviceInfo": { "deviceId": "smart-detector-1.0", "deviceVersion": "1", "deviceTimestamp": "2022-10-11T12:30:03.4467715Z" }, "locationInfo": { "lat": "18.516726", "lon": "73.856255", "timezone": "Coordinated Universal Time" } }'
# PAYLOAD = '{"temperature": {temperature}, "humidityLevel": {humidity}, "mositureLevel": {moisture}}'


FAN_PIN = 26
SPRINKLER_PIN = 18




dht11 = DHT11()
moistureSensor = MoistureSensor()

async def main():
    count = 1
    # GPIO.cleanup()
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(FAN_PIN, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(SPRINKLER_PIN, GPIO.OUT, initial = GPIO.LOW)
    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

        while True:

            try:
                time.sleep(.50)
                moisture = moistureSensor.sense_moisture()

                temp_and_humitidy = dht11.get_dht11_sensor_data()
                temp = temp_and_humitidy[0]
                humidity = temp_and_humitidy[1]
                print('temp', temp, 'humidity: ', humidity)

                data = PAYLOAD.format(temperature=temp, humidity=humidity, moisture=moisture)
                message = Message(data)
                time.sleep(1)

                if moisture < 20:
                    GPIO.output(SPRINKLER_PIN, GPIO.HIGH)
                else:
                    GPIO.output(SPRINKLER_PIN, GPIO.LOW)



                # if temp < 27:
                #     GPIO.output(FAN_PIN, GPIO.LOW)
                # else:
                #     GPIO.output(FAN_PIN, GPIO.HIGH)

                # GPIO.output(SPRINKLER_PIN, GPIO.HIGH)
                # time.sleep(1)
                # GPIO.output(SPRINKLER_PIN, GPIO.LOW)

                # if moisture < 20:
                #     GPIO.output(SPRINKLER_PIN, GPIO.HIGH)
                # else:
                #     GPIO.output(SPRINKLER_PIN, GPIO.LOW)

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



if __name__ == '__main__':

    try:
        asyncio.run(main())
    except Exception as error:
        print("Exception in main" + error.args[0])

        print("Cleaning up GPIO ..")
        GPIO.cleanup()

    print("Cleaning up GPIO ..")
    GPIO.cleanup()
