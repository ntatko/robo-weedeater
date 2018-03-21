#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time

class Mower:

    def __init__(self):

        self.mh = Adafruit_MotorHAT(addr=0x60)
        self._m1 = self.mh.getMotor(1)
        self._m2 = self.mh.getMotor(2)
        self._m3 = self.mh.getMotor(3)

        self._m1.setSpeed(0)
        self._m2.setSpeed(0)
        self._m3.setSpeed(0)

        self._driveConstant = 1
        self._rotationConstant = 1

    def turnOffMotors(self):

        self._m1.run(Adafruit_MotorHAT.RELEASE)
        self._m2.run(Adafruit_MotorHAT.RELEASE)
        self._m3.run(Adafruit_MotorHAT.RELEASE)

    def drive(self, x1 = 0, y1 = 0, x2 = 0):

    	W1 = ((-1/2*x1 - y1*(3**0.5)/2)*self._driveConstant + x2*self._rotationConstant)*255
    	W2 = ((-1/2*x1 + y1*(3**0.5)/2)*self._driveConstant + x2*self._rotationConstant)*255
    	W3 = (x1*self._driveConstant*1.75 + x2*self._rotationConstant)*255

        if W1 > 255:
            W1 = 255
        if W2 > 255:
            W2 = 255


        print("[" + str(W1) + ", " + str(W2) + ", " + str(W3) + "]") #debug

    	if W1 > 0:
    		self._m1.run(Adafruit_MotorHAT.FORWARD)
    	elif W1 < 0:
    		self._m1.run(Adafruit_MotorHAT.BACKWARD)
    	else:
    		self._m1.run(Adafruit_MotorHAT.RELEASE)

    	if W2 > 0:
    		self._m2.run(Adafruit_MotorHAT.FORWARD)
    	elif W2 < 0:
    		self._m2.run(Adafruit_MotorHAT.BACKWARD)
    	else:
            self._m2.run(Adafruit_MotorHAT.RELEASE)

    	if W3 > 0:
    		self._m3.run(Adafruit_MotorHAT.FORWARD)
    	elif W3 < 0:
    		self._m3.run(Adafruit_MotorHAT.BACKWARD)
    	else:
            self._m3.run(Adafruit_MotorHAT.RELEASE)

    	self._m1.setSpeed(abs(int(W1)))
    	self._m2.setSpeed(abs(int(W2)))
    	self._m3.setSpeed(abs(int(W3)))

    	time.sleep(0.01)

    def killCutter(self):
        #this code would stop the cutter from spinning
        print("Motor is killed") #debug

    def spinCutter(self):
        #this code will start the cutter
        print("Motor has started") #debug

    def fast(self):
        self._driveConstant = 1
        self._rotationConstant = 1

    def slow(self):
        self._driveConstant = 0.5
        self._rotationConstant = 0.25
