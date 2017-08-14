#####
#Motor Controller
#####

import sys
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

forwardLeft=12
forwardRight=16

reverseLeft=20
reverseRight=21

ON=GPIO.HIGH
OFF=GPIO.LOW


GPIO.setup(forwardLeft, GPIO.OUT)
GPIO.setup(forwardRight, GPIO.OUT)

GPIO.setup(reverseLeft, GPIO.OUT)
GPIO.setup(reverseRight, GPIO.OUT)

def setPin(direction, toggle):
    GPIO.output(direction, toggle)

def forward():
    print("forward")
    setPin(forwardLeft, ON)
    setPin(forwardRight,ON)

def reverse():
    print("reverse")
    setPin(reverseLeft, ON)
    setPin(reverseRight,ON)

def left():
    print("left")
    setPin(reverseLeft, ON)
    setPin(forwardRight,ON)

def right():
    print("right")
    setPin(reverseRight,ON)
    setPin(forwardLeft, ON)

def stop():
    print("stop")
    setPin(forwardLeft, OFF)
    setPin(forwardRight,OFF)
    setPin(reverseLeft, OFF)
    setPin(reverseRight,OFF)

def cleanup():
    print("bye")
    GPIO.cleanup()
    exit()

