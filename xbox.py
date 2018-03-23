# Noah Tatko
# tatkon@rbtrainers.com
#
#	This is a simple class which uses the pygame module
#	to collect xbox controller values WITHOUT needing
#	a video environment. Works with raspbery pi, raspberry
#	pi zero, raspberry pi zero w, and most linux computers.
#
#	PLEASE_NOTE: administrator privelages are needed to
#	run this module, so use
#		sudo python myfile.py
#	to run the file which contains
#		>>>import xboxController
#		-OR-
#		>>>from xboxController import Controller
#
#
#	Sample Usage:
#		controller1 = Controller()
#		x1 = controller1.get_leftX()
#		if controller1.get_A():
#			x2 = controller1.get_rightX()
#


import pygame
import os
os.putenv('SDL_VIDEODRIVER', 'fbcon') #create a virtual graphics inviromment, which
                                          #pygame needs to work
pygame.display.init() #init the pygame module
pygame.joystick.init() #inid the joystick sub_module of pygame

def get_numControllers():
    return pygame.joystick.get_count()

class Controller:

    def __init__(self, joyNum = 0):
        pygame.joystick.Joystick(joyNum).init() #init the controller
        self._joysticks = pygame.joystick.Joystick(joyNum)

    def get_leftX(self):
        pygame.event.pump()
        return self._joysticks.get_axis(0)

    def get_leftY(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(1)

    def get_rightX(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(3)

    def get_rightY(self):
        pygame.event.pump()
        return self._joysticks.get_axis(4)

    def get_LT(self):
	    pygame.event.pump()
        return self._joysticks.get_axis(2)/2 + 1

    def get_RT(self):
	    pygame.event.pump()
	    return self._joysticks.get_axis(5)/2 + 1

    def get_A(self):
	    pygame.event.pump()
        if self._joysticks.get_button(0):
            return 1
        else:
            return -0

    def get_B(self):
	    pygame.event.pump()
        if self._joysticks.get_button(1):
            return 1
        else:
            return -0

    def get_X(self):
	    pygame.event.pump()
        if self._joysticks.get_button(2):
            return 1
        else:
            return -0

    def get_Y(self):
	    pygame.event.pump()
        if self._joysticks.get_button(3):
            return 1
        else:
            return -0

    def get_start(self):
	    pygame.event.pump()
        if self._joysticks.get_button(7):
            return 1
        else:
            return -0

    def get_back(self):
	    pygame.event.pump()
        if self._joysticks.get_button(6):
            return 1
        else:
            return -0

    def get_RB(self):
	    pygame.event.pump()
        if self._joysticks.get_button(5):
            return 1
        else:
            return -0

    def get_LB(self):
	    pygame.event.pump()
        if self._joysticks.get_button(4):
            return 1
        else:
            return -0

    def listen_for_buttons(self):
	    pygame.event.pump()
        for i in range(8):
            if self._joysticks.get_button(i):
                print(i)

    def listen_for_joysticks(self):
        pygame.event.pump()
        string = ''
        for i in range(self._joysticks.get_numaxes()):
        	string += str(i) + ": " + str(self._joysticks.get_axis(i)) + ", "
        print(string)

    def listen_for_hats(self):
        pygame.event.punp()
        string = ''
        for i in range(self._joysticks.get_numhats()):
            string += str(i) + ": " + str(self._joysticks.get_hat(i)) + ", "
        print(string)
