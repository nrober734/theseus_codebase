import serial
#import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
while True:

    read_ser=ser.read(8)
    print(read_ser)
   # if(read_ser=="Hello From Arduino!"):
   #     blink(11)
