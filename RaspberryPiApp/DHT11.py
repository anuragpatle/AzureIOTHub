import time
import board
import adafruit_dht
import psutil

class DHT11:

    # We first check if a libgpiod process is running. If yes, we kill it!
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()


    sensor = adafruit_dht.DHT11(board.D23)

    def get_dht11_sensor_data(self):
        try:
            temp = self.sensor.temperature
            humidity = self.sensor.humidity
            # print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))

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
            print('Temp: ', obj.get_dht11_sensor_data()[0], 'Humidity', obj.get_dht11_sensor_data()[1])
        except Exception as error:
            time.sleep(4.0)
            continue


