import RPi.GPIO as GPIO
import time

class sound_sensor:
  'Class that initializes and uses the big noise sensor for the THESEUS robot'
  
  def __init__(self):
    # init sound sensor
    pin_num = 12
    GPIO.setmode(GPIO.BOARD) # use board pin numbers
    GPIO.setup(pin_num, GPIO.IN)
    
    
  def ambulance_approaching(self):
    # check to see if there is a loud ambulance noise, if so, return true
    if GPIO.input(pin_num)==1:
      return True
