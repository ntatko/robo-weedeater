import xbox
import time

controller = xbox.Joystick()

while 1:
	print(str(controller.leftX()) + ", " + str(controller.leftY()) + ", " + str(controller.rightX()))
	time.sleep(1)
