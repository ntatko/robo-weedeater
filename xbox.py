import pygame
import os

class Controller:
    def __init__(self):
        os.putenv('SDL_VIDEODRIVER', 'fbcon')
        pygame.display.init()
        pygame.joystick.init()
        pygame.joystick.Joystick(0).init()

        self._joysticks = pygame.joystick.Joystick(0)

    def get_leftX(self):
        pygame.event.pump()
        return self._joysticks.get_axis(0)

    def get_leftY(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(1)

    def get_rightX(self):
        pygame.event.pump()
        return -self._joysticks.get_axis(3)

    def get_A(self):
        if self._joysticks.get_button(0):
            return 1
        else:
            return -0

    def get_B(self):
        if self._joysticks.get_button(1):
            return 1
        else:
            return -0

    def get_X(self):
        if self._joysticks.get_button(2):
            return 1
        else:
            return -0
