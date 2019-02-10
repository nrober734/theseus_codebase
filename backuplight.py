from picamera import PiCamera
from time import sleep
from yolo_opencv import *
import cv2
import lcm
import datetime
import os

#TODO ambient light processing

class makeYolo:
    def __init__(self,image):
        self.image = image
        self.config = "yolov3.cfg"
        self.weights = "yolov3.weights"
        self.classes = "yolov3.txt"

def colorHelper(north,south,east,west):

    R_avg = .25*(north[0]+south[0]+east[0]+west[0])
    G_avg = .25*(north[1]+south[1]+east[1]+west[1])
    B_avg = .25*(north[2]+south[2]+east[2]+west[2])

    if R_avg>=G_avg and R_avg>=B_avg:
        color = "Red"
    elif G_avg>=B_avg and G_avg>=R_avg:
        color = "Green"

    elif R_avg>=B_avg and G_avg>=B_avg:
        color = "Yellow"

    return color



def get_Color(image):

    #Adjust this shit later
    step = 10
    radius = 10
    image = cv2.imread(image)

    orig = image.copy()
    gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

    #Search around the maxLoc

    #Go north
    north = maxLoc + step
    northVal = image[north]

    #Go south
    south = maxLoc + step
    southVal = image[north]

    #Go east
    east = maxLoc + step
    eastVal = image[north]


    #Go west
    west = maxLoc + step
    westVal = image[north]

    color = colorHelper(northVal,southVal,eastVal,westVal)

    return color



def get_time():

    currentDT = datetime.datetime.now()
    dir = "/home/pi/capture_"+currentDT+".jpeg"
    return dir






camera = PiCamera()
camera.start_preview(fullscreen=False,window=(200,300,400,500))
sleep(1)
#camera.stop_preview()

while 1==1:

    dir = get_time() #image name
    camera.capture(dir)

    #Call the YOLO bro
    yolo_suite = makeYolo(dir)

    [feature_name,box] = execute(yolo_suite)

    yeah_light = False
    if feature_name=="traffic light":
        yeah_light = True


    #send the box to the camera
    camera.zoom = box
    dirNew = get_time()

    #capture the new
    camera.capture(dirNew)

    #call image processing module to return light color
    color = get_Color(dirNew)

    os.delete(dirNew)
    os.delete(dir)

    #publish Tlight LCM
    msg.present = yeah_light
    msg.color = color

    lcm = lcm.LCM()
    lcm.publish("world",msg.encode())
    print("Published!")

    #Reset the camera view
    camera.zoom = [0.0, 0.0, 1.0, 1.0]
    sleep(1) #rate of publishing


camera.stop_recording()
camera.stop_preview()
