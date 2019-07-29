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
GPIO.setmode(GPIO.BOARD)
chan_list_out=[33,35,37]
GPIO.setup(chan_list_out,GPIO.OUT)

# Logic that you write
def main():
	GPIO.output(chan_list_out,1)
	time.sleep(1)
	GPIO.output(chan_list_out,0)
	time.sleep(1)

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