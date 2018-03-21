import xbox
import time
import mowerClass

controller = xbox.Controller()
mower = mowerClass.Mower()

while 1:
	if controller.get_A():
		mower.slow()
	if controller.get_B():
		mower.fast()
	controller.get_X()
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
