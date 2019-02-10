from picamera import PiCamera
from time import sleep

class startCam():

    def __init__(self):
        self.camera = PiCamera()

    def runCam(self):

       self.camera.start_preview(fullscreen=False,window=(100,200,300,400))
       self.camera.start_recording('/home/pi/video1.mjpeg')
       sleep(10)
       self.camera.stop_recording()
       self.camera.stop_preview()
