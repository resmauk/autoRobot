import RPi.GPIO as gpio
import time, os, sys
import pins

def setup():
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #Set up pins from a class
    lmf = 19
    lmb = 21
    rmf = 26
    rmb = 24
    sonar = 8
    trigL = 38
    echoL = 36
    trigR = 37
    echoR = 35
    # Set there categories
    inputs = [trigL,trigR]
    outputs = [sonar,lmf,lmb,rmf,rmb,echoL,echoR]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)
    print('### ALL PINS IMPORTED AND SETUP SUCCESSFULLY ###')

# all the pins we will use
print ('pins are defined')
print ('setup() is ran')
setup()
gpio.cleanup()
