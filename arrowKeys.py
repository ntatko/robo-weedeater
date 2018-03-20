from directionTrail import *
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

def get():
        inkey = _Getch()
        #while(1):
	k=inkey()
	while k:
		#drive(0,0,0,0,motor1,motor2,motor3) 	#break
		x1 = y1 = 0
		if k=='\x1b[A':
        	        y1 = 1
       		elif k=='\x1b[B':
                	y1 = -1
        	elif k=='\x1b[C':
                	x1 = -1
        	elif k=='\x1b[D':
                	x1 = 1
		else:
			exit()
		drive(0, y1, x1, 0, motor1, motor2, motor3)
		k=inkey()
	drive(0,0,0,0,motor1,motor2,motor3)


while 1:
	get()
	time.sleep(0.01)
