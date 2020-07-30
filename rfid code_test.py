#A Simple Program for Rfid school attendance system
#importing raspberrypi GPIO Pin functionalities
import RPi.GPIO as GPIO
#Here iam selecting UART port configuration
import serial
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#UART
data = serial.Serial(port ='/dev/ttyS0',
                     baudrate =9600,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS,
                     )
#TM915-Jogtek module is the UART module.
print("Read EPC by TM915-Jogtek")

try:
    while True:

        print("place the card")
        x= data.read(20)
        if x=="14F61D55058710":
            print("card No: ",X)
            print(" Hi Bharath")
            time(0.5)
            print("   ")
        elif x=="14F61D55058711":
            print("card No: ",X)
            print(" Hi Balaji")
            time(0.5)
            print("   ")
        else:
            print(" Display correct card")
            time(0.2)
            print("  ")

except KeyboardInterrupt:
        data.close()

