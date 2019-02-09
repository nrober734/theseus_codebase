import RPi.GPIO as GPIO
import time
import board
import busio

import adafruit_tcs34725


# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

# initialize color sensors

# take in input and process to determine color


# if input is a light color, line is being sensed
# return true

# if input is a dark color, return false


