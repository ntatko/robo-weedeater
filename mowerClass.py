from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time

class Kiwi_Bot:

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
        elif W1 < -255:
            W1 = -255
        if W2 > 255:
            W2 = 255
        elif W2 < -255:
            W2= -255
        if W3 > 255:
            W3 = 255
        elif W3 < -255:
            W3 = -255

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

    def driveFast(self):
        self._driveConstant = 1
        self._rotationConstant = 1

    def driveSlow(self):
        self._driveConstant = 0.65
        self._rotationConstant = 0.4


class Mower(Kiwi_Bot):

    def __init__(self):
        Kiwi_Bot.__init__(self)
        self._m4 = self.mh.getMotor(4)
        self._cutter = 0
        self._cutterSpeed = 0

    def killCutter(self):
        #this code would stop the cutter from spinning
        print("Motor is killed") #debug
        self._m4.run(Adafruit_MotorHAT.RELEASE)
        self._cutterSpeed = 0
        self._cutter = 0
        self.driveFast()

        self._cutter = 0

    def spinCutter(self):
        #this code will start the cutter
        print("Motor has started") #debug
        self.driveSlow()
        self._m4.run(Adafruit_MotorHAT.FORWARD)
        self._cutterSpeed = 100
        self._cutter = 1
        self._m4.setSpeed(self._cutterSpeed)

    def changeCutterSpeed(self, number):
        self._cutterSpeed += number
        if self._cutterSpeed < 0:
            self.killCutter()
        else:
            if self._cutterSpeed > 255:
                self._cutterSpeed = 255
            self._m4.setSpeed(self._cutterSpeed)


    def getCutter(self):
        return self._cutter
