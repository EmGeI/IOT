# CamJam EduKit 3 - Robotics
# Wii controller remote control script

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Left():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Right():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

StopMotors()
import sys, termios, tty, os, io

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

PIN_LED = 25
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, 0)
button_delay = 0.2

##############################################################
## 
##	DISTANCE
##
#############################################################
pinTrigger = 17
pinEcho = 18
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

def distance():
	GPIO.output(pinTrigger, False)
	time.sleep(0.5)
	GPIO.output(pinTrigger, True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	StartTime = time.time()

	while GPIO.input(pinEcho) == 0:
		StartTime = time.time()

	StopTime = StartTime

	while GPIO.input(pinEcho) == 1:
		StopTime = time.time()
		if StopTime - StartTime >= 0.04:
			StopTime = StartTime
			break

	ElapsedTime = StopTime - StartTime
	Distance = ElapsedTime * 34326
	Distance = Distance / 2
	return Distance

for x in range(0,3):
    GPIO.output(PIN_LED, 1)
    time.sleep(0.25)
    GPIO.output(PIN_LED, 0)
    time.sleep(0.25)

while True:
    distance()
    char = getch()

    if (char == "q"):
        StopMotors()
        exit(0)  

    if (char == "s"):
        print('Left pressed')
        Left()
        time.sleep(button_delay)

    if (char == "f"):
        print('Right pressed')
        Right()
        time.sleep(button_delay)          

    elif (char == "d"):
        print('Up pressed')
        Forwards()       
        time.sleep(button_delay)          
    
    elif (char == "e"):
        print('Down pressed')      
	obstacle = distance()
	print(obstacle)	
	if(obstacle < 20.0):
		StopMotors()
		print("Vous etes trop proche d'un objet. Veuillez reculer \(touche d\)")
	else:
		Backwards()
        time.sleep(button_delay)  
    
    StopMotors()
