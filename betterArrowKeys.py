from mowerClass import *
import keyboard

mower = Mower()
       # inkey = _Getch()
        #while(1):
	#k=inkey()
keyboard.start_recording()
while 1:
		#drive(0,0,0,0,motor1,motor2,motor3) 	#break
	x1 = y1 = 0
	if keyboard.is_pressed('up'):
        	y1 = 1
       	elif keyboard.is_pressed('down'):
                y1 = -1
        elif keyboard.is_pressed('left'):
                x1 = -1
        elif keyboard.is_pressed('right'):
                x1 = 1
	elif keyboard.is_pressed('esc'):
		exit()
	mower.drive(0, y1, x1)
		#k=inkey()
#drive(0,0,0,0,motor1,motor2,motor3
	time.sleep(0.01)
