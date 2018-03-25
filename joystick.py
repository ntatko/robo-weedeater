import xbox
import time
import mowerClass
import sensorClass

controller = xbox.Controller()
mower = mowerClass.Mower()
sensors =  sensorClass.Sensors()

while 1:
	if controller.get_A():
		mower.driveSlow()
	if controller.get_B():
		mower.driveFast()
	if controller.get_start() and mower.getCutter() == 0:
		time.sleep(0.2)
		mower.spinCutter()
	elif controller.get_start() and mower.getCutter() == 1:
		time.sleep(0.2)
		mower.killCutter()
	sensors.refreshData()
	print(str(sensors.get_compassHeading()))
	mower.drive(controller.get_leftX(), controller.get_leftY(), controller.get_rightX())
	time.sleep(0.01)
