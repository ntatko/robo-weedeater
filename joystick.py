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
	controller.get_X()
	mower.listen_for_buttons()
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
