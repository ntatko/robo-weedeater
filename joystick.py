import xbox
import time
import mowerClass

controller = xbox.Controller()
mower = Mower()

while 1:
	print(str(controller.get_leftX()) + ", " + str(controller.get_leftY()) + ", " + str(controller.get_rightX()))
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
