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
           self. THESEUS_direction.forward(speed)

    def forward_right(self, time, speed):
        for i in range(time):
            self.THESEUS_direction.forward(speed)
            self.THESEUS_turning.forward(speed);

    def forward_left(self, time, speed):
        for i in range(time):
            self.THESEUS_direction.forward(speed)
            self.THESEUS_turning.backward(speed)

    def all_stop(self):
        self.THESEUS_direction.stop()
        self.THESEUS_turning.stop()

