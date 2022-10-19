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

CONNECTION_STRING="HostName=ih-greenhouse.azure-devices.net;DeviceId=RaspberryPI-1;SharedAccessKey=4EbDwtR+WfC2Qn+sFeDoqzTQ8crPNkMI+MPJCgOrrkA="

DELAY = 5
TEMPERATURE = 20.0
HUMIDITY = 60
PAYLOAD = '{{"temperature": {temperature}, "humidity": {humidity}, "moisture": {moisture}}}'


FAN_PIN = 24
SPRINKLER_PIN = 25

moistureSensor = MoistureSensor()

dht11 = DHT11()


async def main():
    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

        # # Initialize GPIO
        # GPIO.setwarnings(False)
        # GPIO.setmode(GPIO.BCM)
        # GPIO.cleanup()

        while True:

            try:
                moisture = moistureSensor.sense_moisture()
                print ('moisture: ', moisture)
                time.sleep(.50)

                temp_and_humitidy = dht11.get_dht11_sensor_data()
                print('temp', temp_and_humitidy[0], 'humidity: ', temp_and_humitidy[1])

                data = PAYLOAD.format(temperature=temp_and_humitidy[0], humidity=temp_and_humitidy[1], moisture=moisture)
                message = Message(data)

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
