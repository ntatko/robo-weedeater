from mowerClass import *
import keyboard

mower = Mower()
atexit.register(mower.turnOffMotors())

while 1:
	x1 = y1 = 0
	if keyboard.KeyboardEvent: #maybe?
		if keyboard.is_pressed('w'):
		        y1 = 1
       		elif keyboard.is_pressed('s'):
            		y1 = -1
        	if keyboard.is_pressed('a'):
            		x1 = -1
        	elif keyboard.is_pressed('d'):
            		x1 = 1
		if keyboard.is_pressed('space'):
			exit()
	mower.drive(0, y1, x1)
	time.sleep(0.01)
