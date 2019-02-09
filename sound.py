import RPi.GPIO as GPIO
import time

class sound_sensor:
  'Class that initializes and uses the big noise sensor for the THESEUS robot'
  
  def __init__(self):
    # init sound sensor
    pin_num = 12
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_num, GPIO.IN)
    
    
  def ambulance_approaching(self):
    # check to see if there is a loud ambulance noise, if so, return true
    clock = 0
    total = 0
    while clock != 100:
      clock += GPIO.input(pin_num)
      total += 1
      
    if clock / total > 0.75:
      return true
    else:
      return false
