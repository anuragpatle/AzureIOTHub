# # Install libraries.
# pip3 install adafruit-circuitpython-mcp3xxx
# To install system-wide (this may be required in some cases):
# sudo pip3 install adafruit-circuitpython-mcp3xxx

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Soil Moisture
class MoistureSensor:

	MAX_ADC_VALUE = 65472 # Minimum conductivity between the ecletrodes (Air)
	MIN_ADC_VALUE = 16640 # Maximum conductivity between the electrodes (Salty water)

	# create the spi bus
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

	# create the cs (chip select)
	cs = digitalio.DigitalInOut(board.D5)

	# create the mcp object
	mcp = MCP.MCP3008(spi, cs)

	def sense_moisture(self):
		# create an analog input channel on pin 0
		chan = AnalogIn(self.mcp, MCP.P0)

		moisturePercentage =  ((self.MAX_ADC_VALUE - chan.value) / self.MAX_ADC_VALUE) * 100

		# print('Raw ADC Value: ', chan.value)
		# print('Percentage Moisture: ', ((self.MAX_ADC_VALUE - chan.value) / self.MAX_ADC_VALUE) * 100)
		# print('ADC Voltage: ' + str(chan.voltage) + 'V')

		return moisturePercentage




if __name__ == "__main__":
    obj = MoistureSensor()

    while True:
    	print('Moisture: ', obj.sense_moisture())
