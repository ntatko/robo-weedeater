from mowerClass import *
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get(robot):
        inkey = _Getch()
        #while(1):
	k=inkey()
	while k:
		#drive(0,0,0,0,motor1,motor2,motor3) 	#break
		x1 = x2 = y1 = 0
		if k=='\x1b[A':
        	        y1 = 1
       		elif k=='\x1b[B':
                	y1 = -1
        	elif k=='\x1b[C':
                	x2 = -1
        	elif k=='\x1b[D':
                	x2 = 1
		else:
			robot.drive()
			exit()
		robot.drive(x1, y1, x2)
		k=inkey()

mower = Mower()
while 1:
	get(mower)
	time.sleep(0.01)
