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
GPIO.setmode(GPIO.BOARD)
chan_list_out=[33,35,37]
GPIO.setup(chan_list_out,GPIO.OUT,initial=0)
chan_list_in = [38,40]
GPIO.setup(chan_list_in,GPIO.IN)
binary=list(itertools.product(range(2),repeat=3))
k=0
 # add rising edge detection on a channel
GPIO.add_event_detect(40, GPIO.RISING, bouncetime=400)
GPIO.add_event_detect(38,GPIO.RISING, bouncetime=400)
#Logic that you write
def main():
	def setLEDs():
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
	def up():
		global k
		k+=1
		if k==8:
			k=0
	def down():
		global k
		k-=1
		if k==-1:
			k=7
	def down_pressed():
		down()
		setLEDs()

	if GPIO.event_detected(40):
		print('Down pressed')
	if GPIO.event_detected(38):
		print("Up pressed")

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
