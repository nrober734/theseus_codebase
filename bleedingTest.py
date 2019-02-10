from picamera import PiCamera
from time import sleep
from gpiozero import Robot
#from rgb import *
from sound import *
from gpiozero import LED
import keyboard


THESEUS = Robot(left=(24,8), right=(9,22))

#Start the camera


def runTheseus(bot,speed,command):

    #command = input("Enter command: ")

    while 1==1:

        command = input(" ")
        if command=="w":
            bot.forward(speed)
        elif command=="a":
            bot.left(speed)
        elif command=="d":
            bot.right(speed)
        elif command=="s":
            break

speed = 1

while 1==1:


    command = input("Enter command: ")
    runTheseus(THESEUS,speed,command)
