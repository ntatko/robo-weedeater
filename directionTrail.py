#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import math

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


motor1 = mh.getMotor(1)
motor2 = mh.getMotor(2)
motor3 = mh.getMotor(3)

# set the speed to start, from 0 (off) to 255 (max speed)
motor1.setSpeed(0)
motor2.setSpeed(0)
motor3.setSpeed(0)

def drive(x1, y1, x2, y2, m1, m2, m3, mode = 0):
	driveConstant = 0.75
	rotationConstant = 0.25

	W1 = ((-1/2*x1 - y1*(3**0.5)/2)*driveConstant + x2*rotationConstant)*255
	W2 = ((-1/2*x1 + y1*(3**0.5)/2)*driveConstant + x2*rotationConstant)*255
	W3 = (x1*driveConstant + x2*rotationConstant)*255

	if mode == 1:
		W1 = W1*0.7
		W2 = W2*0.7
		W3 = W3*1.3

	#for x1 = 1
	# int(((-1/2(1) - 0)*0.75)*255) = -95.625

	print("[", W1, ", ", W2, ", ", W3, "]")

	if W1 > 0:
		m1.run(Adafruit_MotorHAT.FORWARD)
	elif W1 < 0:
		m1.run(Adafruit_MotorHAT.BACKWARD)
	else:
		m1.run(Adafruit_MotorHAT.RELEASE)
	if W2 > 0:
		m2.run(Adafruit_MotorHAT.FORWARD)
	elif W2 < 0:
		m2.run(Adafruit_MotorHAT.BACKWARD)
	else:
                m2.run(Adafruit_MotorHAT.RELEASE)
	if W3 > 0:
		m3.run(Adafruit_MotorHAT.FORWARD)
	elif W3 < 0:
		m3.run(Adafruit_MotorHAT.BACKWARD)
	else:
                m3.run(Adafruit_MotorHAT.RELEASE)

	m1.setSpeed(abs(int(W1)))
	m2.setSpeed(abs(int(W2)))
	m3.setSpeed(abs(int(W3)))

	time.sleep(0.01)

drive(0, 0, 0, 0, motor1, motor2, motor3)


def turnLeft(degrees):
	turn = degrees % 360
	for i in range(int(turn/3.125)):
		drive(0,0,1,0,motor1,motor2,motor3)
	drive(0,0,0,0,motor1,motor2,motor3)

def turnRight(degrees):
	turn = degrees % 360
	for i in range(int(turn/3.125)):
		drive(0,0,-1,0,motor1,motor2,motor3)
	drive(0,0,0,0,motor1,motor2,motor3)
def forward(feet):
	for i in range(feet):
		for j in range(int(18)):
			drive(0,1,0,0,motor1,motor2,motor3)
	drive(0,0,0,0,motor1,motor2,motor3)
def backward(feet):
	for i in range(feet):
		for j in range(int(18)):
			drive(0,-1,0,0,motor1,motor2,motor3)
	drive(0,0,0,0,motor1,motor2,motor3)
def straifRight(feet):
	for i in range(int(feet*2)):
		drive(1,0,0,0,motor1,motor2,motor3,1)
	drive(0,0,0,0,motor1,motor2,motor3)
def straifLeft(feet):
	for i in range(int(feet*2)):
		drive(-1,0,0,0,motor1,motor2,motor3,1)
	drive(0,0,0,0,motor1,motor2,motor3)
