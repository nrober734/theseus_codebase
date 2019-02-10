#THESEUS 2019
#Sensor Server

from multiprocessing import Queue
from multiprocessing import Process

#LCM
import lcm

#TODO specific lcm type import statements (world model)

#Camera
from picamera import PiCamera
from time import sleep

#RGB
import time
import board
import busio
import adafruit_tcs34725
import serial

#Big noise
import RPi.GPIO as GPIO
import sound

def get_RGB(q):

    return rgb
    #from amtuko

def get_bignoise(q):

    soundCheck = sound_sensor()
    ambulance = soundCheck.ambulance_approaching()

    return ambulance



def store_world(R,G,B,soundLevel,tLight):

    msg = world_t()
    msg.R = R
    msg.G = G
    msg.B = B
    msg.soundLevel = soundLevel
    msg.trafficLight = tLight
    return msg


#Setup the threads



#*****Main runtime******

q_RGB = Queue()
q_bigNoise = Queue()

#Launch the RGB thread
p1 = Process(target=get_RGB,args=(q_RGB,))
p2 = Process(target=get_bignoise,args=(q_bigNoise,))

p1.start()
p2.start()
#p3.start() thread for camera listening

#Launch the big noise thread


while 1==1:

    RGB = que_RGB.get()
    ambulance = que_bigNoise.get()

    #Subscribe to the traffic light from the camera controller

    #tLightStatus
    print("RGB sent: "+RGB[0] + " "RGB[1] + " "+RGB[2] + " ")
    print("Ambulance: "+ambulance)

    #store world
    msg = store_world(RGB[0],RGB[1],RGB[2],ambulance,tLightStatus)
    lcm = lcm.LCM()
    lcm.publish("world",msg.encode())
    print("Published!")
    sleep(1) #rate of publishing






#----------------
