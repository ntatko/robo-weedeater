import xbox
import time
import mowerClass

controller = xbox.Controller()
mower = mowerClass.Mower()

while 1:
	if controller.get_A():
		mower.driveSlow()
	if controller.get_B():
		mower.driveFast()
	if controller.get_start() and not mower.getCutter():
		time.sleep(0.2)
		mower.spinCutter()
	elif controller.get_start() and mower.getCutter():
		time.sleep(0.2)
		mower.killCutter()
	elif controller.get_Y() and mower.getCutter():
		time.sleep(0.1)
		mower.changeCutterSpeed(25)
	elif controller.get_X() and mower.getCutter():
		time.sleep(0.1)
		mower.changeCutterSpeed(-25)
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
