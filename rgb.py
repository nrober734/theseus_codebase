import RPi.GPIO as GPIO
import time
import board
import busio

import adafruit_tcs34725

class rgb_sensor:
  'Class to initialize and use the rgb sensors for the THESEUS robot'
  def __init__(self):
    # Initialize I2C bus and sensor.
    i2c = busio.I2C(board.SCL, board.SDA)
    self.sensor = adafruit_tcs34725.TCS34725(i2c)
    
  def process_input(self):
    # take in input and process to determine color
    
    # if input is a light color, line is being sensed, return true
    
    # if input is a darker color, line is not sensed, return false


#combine 3 sensors, return 


# helper functions, convert input to RGB values, limits on what is considered dark/light

