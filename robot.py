from gpiozero import Robot
from rgb import *
from sound import *
from gpiozero import LED


class THESEUS:
    'class that controls the motor on the robot'
    THESEUS_turning = Robot(left=(,), right=(,))
    THESEUS_direction = Robot(left=(,), right=(,))
    
    def __init__(self):

    def forward_straight(self, time, speed):
        for i in range(time):
            THESEUS_direction.forward(speed)

    def forward_right(self, time):
        for i in range(time):
            THESEUS_direction.forward(speed)
            THESEUS_turning.forward(speed);

    def forward_left(self, time):
        for i in range(time):
            THESEUS_direction.forward(speed)
            THESEUS_turning.backward(speed)

    def all_stop(self):
        THESEUS_direction.stop()
        THESEUS_turning.stop()

