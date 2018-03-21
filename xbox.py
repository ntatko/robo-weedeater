#import pygame
#import time

#class Controller:

#    def __init__(self):
#        pygame.init()
#        pygame.joystick.init()
#
#        self._controllerObj = pygame.Joystick(0)
#        self._joyCount = self._controllerObj.get_init()
#
#        self._joysticks = []
#
#    def leftX(self):
#        return self._controllerObj.



import pygame

os.putenv('SDL_VIDEODRIVER', 'fbcon')
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print "Name of the joystick:"
print JoyName
# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print "Number of axis:"
print JoyAx

# Prints the values for axis0
while True:
        pygame.event.pump()
        print pygame.joystick.Joystick(0).get_axis(0)
