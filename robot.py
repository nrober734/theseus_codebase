from gpiozero import Robot
from rgb import *
from sound import *

<<<<<<< HEAD
robby = Robot(left=(24,8), right=(9,22))

#print("fuck off")

while 1==1:
	robby.forward(.5)
	#robby.right()

	print("fuck off")

=======

# initialize robot w/ correct pin numbers
THESEUS = Robot(left=(7,8), right=(9,10))
MAX_SPEED = 0.5
stay_in_lane = True

# initialize all sensors on the robot
rgb1 = rbg_sensor()
rgb2 = rbg_sensor()
rgb3 = rbg_sensor()

# until we stop the robot, continue looping

# check to make sure robot is within lines, if not, adjust

# if robot isn't turning, ensure that the blinker is off

# if robot is turning, turn on the correct blinker

# check to make sure there isn't an ambulance noise
# if so, pull over and stop until it stops

# if photoresistor detects limited visibility, turn on headlamps
# also begin tracking to centerline instead of lane markers
stay_in_lane = False


# if we end program, stop robot
THESEUS.stop()
>>>>>>> 8714f619f2ac1643e85ac506b1c851695bb23792

