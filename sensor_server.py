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

left_serial = serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
left_serial.baudrate = 9600

right_serial = serial.Serial("/dev/ttyACM1",9600)  #change ACM number as found from ls /dev/tty/ACM*
right_serial.baudrate = 9600

center_sensor = rgb_sensor()
center_sensor.init_rp_sensor()



def get_RGB(q):
    left_sensor =  rgb_sensor()
    left_rgb = left_sensor.ardu_RGB_input(left_serial)
    center_rgb = center_sensor.process_input()
    right_sensor = rgb_sensor()
    right_rgb = right_sensor.ardu_RGB_input(right_serial)
    if left_rgb.error_skip(left_rgb,left_serial) or right_rgb.error_skip(right_rgb,right_serial):
        rgb = [left_rgb, center_rgb, right_rgb]

    return rgb

def get_bignoise(q):

    soundCheck = sound_sensor()
    ambulance = soundCheck.ambulance_approaching()

    return ambulance

def get_lighting(q):



def store_world(R,G,B,soundLevel,tLight, photoR):

    msg = world_t()
    msg.R = R
    msg.G = G
    msg.B = B
    msg.soundLevel = soundLevel
    msg.trafficLight = tLight
    msg.photoResistor = photoR
    return msg


#Setup the threads



#*****Main runtime******

q_RGB = Queue()
q_bigNoise = Queue()
q_lighting = Queue()

#Launch the RGB thread
p1 = Process(target=get_RGB,args=(q_RGB,))
p2 = Process(target=get_bignoise,args=(q_bigNoise,))
p3 = Process(target=get_lighting,args=(q_lighting,))

p1.start()
p2.start()
p3.start()
#p4.start() thread for camera listening

#Launch the big noise thread


while 1==1:

    RGB = q_RGB.get()
    ambulance = q_bigNoise.get()
    lighting = q_lighting.get()
    #Subscribe to the traffic light from the camera controller

    #tLightStatus
    print("RGB sent: "+RGB[0] + " "RGB[1] + " "+RGB[2] + " ")
    print("Ambulance: "+ambulance)

    #store world
    msg = store_world(RGB[0],RGB[1],RGB[2],ambulance,tLightStatus, lighting)
    lcm = lcm.LCM()
    lcm.publish("world",msg.encode())
    print("Published!")
    sleep(1) #rate of publishing






#----------------
