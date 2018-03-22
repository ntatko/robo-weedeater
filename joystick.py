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
	if controller.get_start() and mower.getCutter() == 0:
		while controller.get_start():
			time.sleep(0.01)
		mower.spinCutter()
	elif controller.get_start() and mower.getCutter() == 1:
		while controller.get_start():
			time.sleep(0.01)
		mower.killCutter()
	controller.get_X()
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
