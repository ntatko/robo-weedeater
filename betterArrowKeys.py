from mowerClass import *
import keyboard

mower = Mower()
atexit.register(mower.turnOffMotors())
       # inkey = _Getch()
        #while(1):
	#k=inkey()
keyboard.start_recording()
while 1:
		#drive(0,0,0,0,motor1,motor2,motor3) 	#break
	x1 = y1 = 0
	if keyboard.KeyboardEvent: #maybe?
		if keyboard.is_pressed('w'):
	        	y1 = 1
       	elif keyboard.is_pressed('s'):
                y1 = -1
        elif keyboard.is_pressed('a'):
                x1 = -1
        elif keyboard.is_pressed('d'):
                x1 = 1
		elif keyboard.is_pressed('space'):
			exit()
	mower.drive(0, y1, x1)
		#k=inkey()
#drive(0,0,0,0,motor1,motor2,motor3
	time.sleep(0.01)
