#####
#Motor Controller
#####

import sys
import time
import RPi.GPIO as GPIO
import pygame

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
    return "done"

def setDirection(key, state):
    if key==pygame.K_w:
        if state is not "forward":
            forward()
            state = "forward"

    elif key==pygame.K_a:
        if state is not "left":
            left()
            state = "left"

    elif key==pygame.K_s:
        if state is not "reverse":
            reverse()
            state = "reverse"

    elif key==pygame.K_d:
        if state is not "right":
            right()
            state = "right"
    elif key==pygame.K_ESCAPE:
        state = cleanup()
        
    return state


pygame.init()
pygame.display.set_mode((100,100))

done=False
state="stop"
directions = [pygame.K_d, pygame.K_s, pygame.K_a, pygame.K_w]

start = time.time()
end = time.time()

print(directions)


while not done:
    events = pygame.event.get()
    if not events:
        end = time.time()
        elapsed = end - start
        if elapsed > 0.05:
            if state is not "stop":
                stop()
                state = "stop"
    else:
        for event in events:
            if event.type == pygame.KEYDOWN:
                state = setDirection(event.key, state)
                break
        start = time.time()
    
exit()
