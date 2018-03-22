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
            print("got x")
            return 1
        else:
            return -0

    def get_Y(self):
        if self._joysticks.get_button(3):
            print("got y")
            return 1
        else:
            return -0

    def get_start(self):
        if self._joysticks.get_botton(4):
            print("got start")
            return 1
        else:
            return -0

    def get_back(self):
        if self._joysticks.get_button(5):
            print("got back")
            return 1
        else:
            return -0

    def get_menu(self):
        if self._joysticks.get_button(6):
            print("got menu")
            return 1
        else:
            return -0
