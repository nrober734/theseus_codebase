from rbg import *
from config import *
import serial

def main():
    ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
    ser.baudrate = 9600

    ruthbaderginsberg = rgb_sensor()
    results = ruthbaderginsberg.ardu_input(ser)

    for i in results:
        print(i)

        
