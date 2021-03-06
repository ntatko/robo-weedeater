
import socket, traceback, string
from sys import stderr
from numpy import arcsin
import math

def prepare(numbers):
    while numbers[0] == ' ':
        numbers = numbers[1:]
    return numbers

class Sensors:

    def __init__(self):

        self._data = []

        self._originCompass = []
        self._headingMode = 0
        self._heading = 0.0

        self._thisCompass = []
        self._thisAccelerometer = []
        self._thisGPS = []
        self._thisGyro = []

        self._lastCompass = []
        self._lastAccelerometer = []
        self._lastGPS = []
        self._lastGyro = []

        self._host = ''
        self._port = 5555
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._s.bind((self._host, self._port))

        try:

            while self._originCompass == []:
                self._message, self._address = self._s.recvfrom(8192)
                self._data = self._message.split( "," )
                if ' 5' in self._data:
                    self._lastCompass = self._thisCompass
                    self._thisCompass = [float(prepare(self._data[self._data.index(' 5') + 1])), float(prepare(self._data[self._data.index(' 5') + 2])), float(prepare(self._data[self._data.index(' 5') + 3]))]
		    print(str(self._thisCompass))
                    self._originCompass = self._thisCompass

            if '  1' in self._data:
                self._lastGPS = self._thisGPS
                self._thisGPS = [float(prepare(self._data[self._data.index(' 1') + 1])), float(prepare(self._data[self._data.index(' 1') + 2])), float(prepare(self._data[self._data.index(' 1') + 3]))]

            if ' 3' in self._data:
                self._lastAccelerometer = self._thisAccelerometer
                self._thisAccelerometer = [float(prepare(self._data[self._data.index(' 3') + 1])), float(prepare(self._data[self._data.index(' 3') + 2])), float(prepare(self._data[self._data.index(' 3') + 3]))]

            if ' 4' in self._data:
                self._lastGyro = self._thisGyro
                self._thisGyro = [float(prepare(self._data[self._data.index(' 4') + 1])), float(prepare(self._data[self._data.index(' 4') + 2])), float(prepare(self._data[self._data.index(' 4') + 3]))]

        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()

    def refreshData(self):
        try:
            self.refreshConnection()
            self._message, self._address = self._s.recvfrom(8192)
            self._data = self._message.split( "," )

            if ' 1' in self._data:
                self._lastGPS = self._thisGPS
                self._thisGPS = [float(prepare(self._data[self._data.index(' 1') + 1])), float(prepare(self._data[self._data.index(' 1') + 2])), float(prepare(self._data[self._data.index(' 1') + 3]))]

            if ' 3' in self._data:
                self._lastAccelerometer = self._thisAccelerometer
                self._thisAccelerometer = [float(prepare(self._data[self._data.index(' 3') + 1])), float(prepare(self._data[self._data.index(' 3') + 2])), float(prepare(self._data[self._data.index(' 3') + 3]))]

            if ' 4' in self._data:
                self._lastGyro = self._thisGyro
                self._thisGyro = [float(prepare(self._data[self._data.index(' 4') + 1])), float(prepare(self._data[self._data.index(' 4') + 2])), float(prepare(self._data[self._data.index(' 4') + 3]))]

            if ' 5' in self._data:
                self._lastCompass = self._thisCompass
                self._thisCompass = [float(prepare(self._data[self._data.index(' 5') + 1])), float(prepare(self._data[self._data.index(' 5') + 2])), float(prepare(self._data[self._data.index(' 5') + 3]))]

        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()

    def refreshConnection(self):
        self._s.shutdown()
        self._s.close()

        self._host = ''
        self._port = 5555
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._s.bind((self._host, self._port))

    def get_compass(self):
        return self._thisCompass

    def get_accelerometer(self):
        return self._thisAccelerometer

    def get_gps(self):
        return self._thisGPS

    def get_gyro(self):
        return self._thisGyro

    def get_changeCompass(self):
        return [self._lastCompass[0] - self._thisCompass[0], self._lastCompass[1] - self._thisCompass[1], self._lastCompass[2] - self._thisCompass[2]]

    def get_changeAccelerometer(self):
        return [self._lastAccelerometer[0]-self._thisAccelerometer[0], self._lastAccelerometer[1]-self._thisAccelerometer[1], self._lastAccelerometer[2]-self._thisAccelerometer[2]]

    def get_compassHeading(self):
        while self._thisCompass == []:
            self.refreshData()
        return math.degrees(arcsin((self._originCompass[0]*self._thisCompass[0] + self._originCompass[1]*self._thisCompass[1] +
                self._originCompass[2]*self._thisCompass[2])/(((self._originCompass[0]**2 +
                self._originCompass[1]**2 + self._originCompass[2]**2)**0.5) * (self._thisCompass[0]**2 +
                self._thisCompass[1]**2 + self._thisCompass[2]**2)**0.5)))

    def set_compassHeading(self, heading):
        self._heading = heading
        self._headingMode = 1

    def get_degFromHeading(self, heading):
        return self._heading - heading

    def end_compassHeading(self):
        if self._headingMode == 1:
            self._heading = 0
            self._headingMode = 0

    def printStream(self):
        print str(self._data)
