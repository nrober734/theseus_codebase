from rgb import *
from config import *
import serial

def main():
	ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
	ser.baudrate = 9600

	ruthbaderginsberg = rgb_sensor()
	while True:
    		results = ruthbaderginsberg.ardu_input(ser)
        	print(results)
    # for i in results:
    #     print(i)
