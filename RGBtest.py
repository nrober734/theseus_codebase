# Simple demo of the TCS34725 color sensor.
# Will detect the color from the sensor and print it out every second.
import time

import board
import busio

import adafruit_tcs34725


# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
#sensor2 = adafruit_tcs34725.TCS34725(i2c)



# Main loop reading color and printing it every second.
while True:
    # Read the color temperature and lux of the sensor too.
    temp = sensor.color_temperature
    lux = sensor.lux

 #   temp2 = sensor2.color_temperature
  #  lux2 = sensor2.lux
    print('Temperature Sensor 1: {0}K Lux: {1}'.format(temp,lux))
   # print('Temperature Sensor 2: {0}K Lux: {1}'.format(temp2, lux2))
    # Delay for a second and repeat.
    time.sleep(1.0)
