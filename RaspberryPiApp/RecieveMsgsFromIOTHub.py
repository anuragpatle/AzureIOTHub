import time
from azure.iot.device import IoTHubDeviceClient
import RPi.GPIO as GPIO

RECEIVED_MESSAGES = 0
FAN_PIN = 26 # GPIO 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT, initial = GPIO.LOW)


CONNECTION_STRING = "HostName=ih-greenhouse.azure-devices.net;DeviceId=smart-detector-1.0;SharedAccessKey=0Pbb0a+Of7Ii8ApmsxmVdUTe1FNwOO5pi+eXN7bxKrs="

def message_handler(message):
    global RECEIVED_MESSAGES
    RECEIVED_MESSAGES += 1
    print("")
    print("Message received:")

    # print data from both system and application (custom) properties
    for property in vars(message).items():
        print ("    {}".format(property))

    strMsg = message.data.decode()

    # print(type(strMsg))

    if strMsg == 'MAKE-FAN-ON':
        GPIO.output(FAN_PIN, GPIO.HIGH)
        print('MAKE-FAN-ON')
    else:
        GPIO.output(FAN_PIN, GPIO.LOW)
        print('MAKE-FAN-OFF')


    print("Total calls received: {}".format(RECEIVED_MESSAGES))


def main():
    print ("Starting the Python IoT Hub C2D Messaging device sample...")

    # Instantiate the client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print ("Waiting for C2D messages, press Ctrl-C to exit")
    try:
        # Attach the handler to the client
        client.on_message_received = message_handler

        while True:
            time.sleep(1000)
    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")
    finally:
        # Graceful exit
        print("Shutting down IoT Hub Client")
        client.shutdown()


if __name__ == '__main__':
    main()
