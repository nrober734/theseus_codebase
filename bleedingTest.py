from picamera import PiCamera
from time import sleep
from gpiozero import Robot
from rgb import *
from sound import *
from gpiozero import LED
from camera_controller import *
import keyboard


THESEUS = Robot(left=(24,8), right=(9,22))

#Start the camera
cam = startCam()
cam.runCam()

def runTheseus(bot,speed):

    command = input("Enter command: ")

    while 1==1:

        if command=="w" or keyboard.is_pressed('w'):
            bot.forward(speed)
        elif command=="a" or keyboard.is_pressed('a'):
            bot.left(speed)
        elif command=="d" or keyboard.is_pressed('d')
            bot.right(speed)
        elif command=="s"or keyboard.is_pressed('s')
            break

speed = 1

while 1==1:
    runTheseus(THESEUS,speed))
