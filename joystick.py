import xbox
import time

controller = xbox.Controller()

while 1:
	print(str(controller.get_leftX()) + ", " + str(controller.get_leftY()) + ", " + str(controller.get_rightX()))
	time.sleep(1)
