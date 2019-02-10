from rgb import *
from config import *
import serial



ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600

ruthbaderginsberg = rgb_sensor()
print ("We aboutta go in")
while True:
    print("We made it in bb")
    results = ruthbaderginsberg.ardu_input(ser)
    print(results)
print("We didn't make it in")
    # for i in results:
    #     print(i)
