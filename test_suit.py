from rgb import *
from config import *
import serial



ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600

rbginsberg = rgb_sensor()
print ("We aboutta go in")
    #print("We made it in bb")
#results = rbginsberg.ardu_RGB_input(rbginsberg.raw_ardu_input(ser))
    #results = rbginsberg.raw_ardu_input(ser)
    #print(results)

    var = rbginsberg.ardu_RGB_input(ser)
    print(var)
# results = rbginsberg.raw_ardu_input(ser)
# print(results)
#print("We didn't make it in")
    # for i in results:
    #     print(i)
