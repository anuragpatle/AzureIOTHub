from MoistureSensor import MoistureSensor
from DHT11 import DHT11
import time


moistureSensor = MoistureSensor()

dht11 = DHT11()



while True:

    try:
        print ('moisture: ', moistureSensor.sense_moisture())
        time.sleep(.50)

        temp_and_humitidy = dht11.get_dht11_sensor_data()
        print('temp', temp_and_humitidy[0], 'humidity: ', temp_and_humitidy[1])

    except Exception as error:
        time.sleep(2.0)
        continue


