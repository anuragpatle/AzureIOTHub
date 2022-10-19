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
moisture = "false" 

async def main():
 
    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
 
        # Initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
 
        # Read data using pin GPIO17
        dhtDevice = dht11.DHT11(pin=17)
         
        # GPIO.setup(FAN_PIN, GPIO.OUT)
        # GPIO.setup(SPRINKLER_PIN, GPIO.OUT)

 
        print("Sending serivce started. Press Ctrl-C to exit")
        while True:
            time.sleep(1)
            try:
                #DHT11
                result = dhtDevice.read()
                

                print("result.is_valid(): ", result.is_valid())

                if result.is_valid():
                    temperature = result.temperature
                    humidity = result.humidity
 
                    data = PAYLOAD.format(temperature=temperature, humidity=humidity, moisture=moisture)
                    message = Message(data)
 
                    # Send a message to the IoT hub
                    print(f"Sending message: {message}")
                    await client.send_message(message)
                    print("Message successfully sent")
                else:
                    print("Error: %d" % result.error_code)
                    continue
 
                await asyncio.sleep(DELAY)
 
            except KeyboardInterrupt:
                print("Service stopped")
                GPIO.cleanup()
                break
 
    except Exception as error:
        print(error.args[0])
 
if __name__ == '__main__':
    asyncio.run(main())