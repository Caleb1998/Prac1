#!/usr/bin/python3
"""
Python Practical Template
Caleb Smit
Readjust this Docstring as follows:
Names: Caleb Smit
Student Number: SMTCAL003
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools

GPIO.setmode(GPIO.BOARD) #sets the pin numering system to that of the boards
chan_list_out=[33,35,37] #the pin numbers used for output (connected to LEDs)
GPIO.setup(chan_list_out,GPIO.OUT,initial=0) #sets up the pins as outputs, and sets them low
chan_list_in = [38,40] #the pin nums for input channels
GPIO.setup(chan_list_in,GPIO.IN) #sets the pin numbers listed to outputs
binary=list(itertools.product(range(2),repeat=3)) #creates a list of binary sequences from 000 to 111, (a 2D array)
k=0 #this will be used as the counter
 # add rising edge detection on a channel
GPIO.add_event_detect(40, GPIO.RISING, bouncetime=300) #initializes the intterupt detector on channel 40, waits for rising edge, bnctm for 300ms
GPIO.add_event_detect(38,GPIO.RISING, bouncetime=300) #same as above for channel 38

#Main program
def main():
	def setLEDs(): #function used to set LEDs
		global k
		if binary[k][2]==0:	#lowest bit
			GPIO.output(33,0)
		else:
			GPIO.output(33,1)
		if binary[k][1]==0:	#middle bit
			GPIO.output(35,0)
		else:
			GPIO.output(35,1)
		if binary[k][0]==0:	#highest bit
			GPIO.output(37,0)
		else:
			GPIO.output(37,1)
	def up(): #function used to increment count
		global k
		k+=1
		if k==8: #loops from 7 to 0
			k=0
	def down(): #function used to decrement count
		global k
		k-=1
		if k==-1: #loops from 0 to 7
			k=7
	def down_pressed(): #to be called when dwn button is pressed
		down()
		setLEDs()
	def up_pressed(): #when up button pressed
		up()
		setLEDs()

	if GPIO.event_detected(40):
		#print('Down pressed') ##used for user feedback initially
		down_pressed()
	if GPIO.event_detected(38):
		#print("Up pressed")
		up_pressed()

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
       		main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
