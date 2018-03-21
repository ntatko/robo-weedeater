import pygame
import os

class Controller:
    def __init__(self):
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

        self._controller = pygame.joystick.Joystick(0)

    def get_leftX(self):
        pygame.event.pump()
        return self._controller.get_axis(0)

    def get_leftY(self):
        pygame.event.pump()
        return -self._controller.get_axis(1)

    def get_rightX(self):
        pygame.event.pump()
        return self._controller.get_axis(3)
