import time
import board
import adafruit_dht
import psutil
import RPi.GPIO as GPIO


class DHT11:

    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()


    sensor = adafruit_dht.DHT11(board.D23) # Pin 16 or GPIO 23 is data pin of DHT11 sensor

    def get_dht11_sensor_data(self):
        try:
            temp = self.sensor.temperature
            humidity = self.sensor.humidity
            print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
            return temp, humidity

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)

        except Exception as error:
            self.sensor.exit()
            raise error
            time.sleep(2.0)


if __name__ == "__main__":
    obj = DHT11()

    while True:
        try:
            time.sleep(1.0)
            obj.get_dht11_sensor_data()
        except Exception as error:
            time.sleep(4.0)
            continue


