from picamera import PiCamera
from time import sleep

class startCam():

    def __init__(self):
        self.camera = PiCamera()

    def runCam(self):

        start_preview(fullscreen=False,window=(100,200,300,400))
        camera.start_recording('/home/pi/video1.h264')
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()
