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
	if controller.get_start() and controller.getCutter():
		mower.spinCutter()
	elif controller.getStart() and !controller.getCutter():
	controller.get_X()
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
