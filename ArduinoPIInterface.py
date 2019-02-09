import serial
#import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):
<<<<<<< HEAD
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
return
=======


#GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
#GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return
>>>>>>> dcbdc885ad884284036fc0c9932a23249ef14e6f

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.OUT)
while True:

<<<<<<< HEAD
    read_ser=ser.readline()
    print(read_ser)
    if(read_ser=="Hello From Arduino!"):
        blink(11)
=======
	read_ser=ser.readline()
	print(read_ser)
	if(read_ser=="Hello From Arduino!"):
		print("ur ugly")
>>>>>>> dcbdc885ad884284036fc0c9932a23249ef14e6f
