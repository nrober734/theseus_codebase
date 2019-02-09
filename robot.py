from gpiozero import Robot

# initialize robot w/ correct pin numbers
THESEUS = Robot(left=(7,8), right=(9,10))
MAX_SPEED = 0.5

# initialize all sensors on the robot


# until we stop the robot, continue looping

# check to make sure robot is within lines, if not, adjust

# if robot isn't turning, ensure that the blinker is off

# if robot is turning, turn on the correct blinker

# check to make sure there isn't an ambulance noise
# if so, pull over and stop until it stops

# if photoresistor detects limited visibility, turn on headlamps
# also begin tracking to centerline instead of lane markers


# if we end program, stop robot
THESEUS.stop()

