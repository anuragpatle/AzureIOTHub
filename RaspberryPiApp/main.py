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
PAYLOAD = '{{"temperature": {temperature}, "humidity": {humidity}, "moisture": {moisture}}}'


FAN_PIN = 2
SPRINKLER_PIN = 26

# moistureSensor = MoistureSensor()
# GPIO.cleanup()
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(FAN_PIN, GPIO.OUT)

dht11 = DHT11()

async def main():
    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

        while True:

            try:
                # moisture = moistureSensor.sense_moisture()
                # print ('moisture: ', moisture)
                time.sleep(.50)

                temp_and_humitidy = dht11.get_dht11_sensor_data()
                temp = temp_and_humitidy[0]
                humidity = temp_and_humitidy[1]
                print('temp', temp, 'humidity: ', humidity)

                data = PAYLOAD.format(temperature=temp, humidity=humidity, moisture="moisture")
                message = Message(data)

                # if temp <= 27:
                #     GPIO.output(FAN_PIN, GPIO.HIGH)
                # else:
                #     GPIO.output(FAN_PIN, GPIO.LOW)

                # Send a message to the IoT hub
                print(f"Sending message: {message}")
                await client.send_message(message)
                print("Message successfully sent")

            except Exception as error:
                time.sleep(2.0)
                continue


    except Exception as error:
        print(error.args[0])



if __name__ == '__main__':
    asyncio.run(main())
