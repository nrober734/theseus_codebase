#THESEUS 2019
#Decision making module

#LCM
import lcm

#TODO specific lcm type import statements (world model)

#Camera
from picamera import PiCamera
from time import sleep

from lights import *

#RGB
import time
import board
import busio
import adafruit_tcs34725
import serial
from rgb import *

#Big noise
import RPi.GPIO as GPIO
from sound import *


# returns 0 if continuing straight, 1 if should turn left, 2 if should turn right
# if turning, will also return a non-zero value of intensity
def choose_direction(world_state, centerline, num_intersections):
    left_on_line = on_line(world_state.LEFT[0], world_state.LEFT[1], world_state.LEFT[2])
    center_on_line = on_line(world_state.CENTER[0], world_state.CENTER[1], world_state.CENTER[2])
    right_on_line = on_line(world_state.RIGHT[0], world_state.RIGHT[1], world_state.RIGHT[2])
    if left_on_line:
        if center_on_line:
            #we have reached an intersection, determine what to do
            if num_intersections < 2:
                return (1, high_speed)
            else:
                return (2, high_speed)
        else:
            # correct left
            return (1, low_speed)
                
    elif center_on_line:
        if right_on_line:
            #we have reached an intersection
            if num_intersections < 2:
                return (1, high_speed)
            else:
                return (2, high_speed)
        else:
            return (0, 0)
    else:
        return (2, low_speed)



def make_decision(state, centerline):
    intersection_count = 0
    if state.soundLevel == True:
        # pull the fuck over
        robot.forward_right(1, high_speed)
        robot.all_stop()

    elif state.photoResistor == True:
        # turn on headlights
        light.headlamps(True)
    else:
        # turn off headlights
        light.headlamps(False)
        if state.trafficLight == 4 or state.trafficLight == 3:
            direction_and_speed = choose_direction(state, centerline, intersection_count)
            if direction_and_speed[0] == 0:
                robot.forward_straight(1,1)
            elif direction_and_speed[0] == 1:
                light.turn_left()
                robot.forward_left(1, direction_and_speed[1])
            else:
                light.turn_right()
                robot_forward_right(1, direction_and_speed[1])
        else:
            # light is yellow or red, so  stop
            robot.all_stop()

            
