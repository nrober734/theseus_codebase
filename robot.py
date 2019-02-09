from gpiozero import Robot

robby = Robot(left=(7,8), right=(9,10))
robby.forward(0.4)
robby.right(0.4)

## e.g. change
robby = Robot(left=(7,8), right=(9,10))
## to
robby = Robot(left=(9,10), right=(7,8))

robby.forward(0.4)

## e.g. change
robby = Robot(left=(9,10), right=(7,8))
## to
robby = Robot(left=(9 10), right=(8,7))
