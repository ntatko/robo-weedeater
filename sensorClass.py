
import socket, traceback, string
from sys import stderr


class Sensors:

    def __init__(self):
        self._ip = ipAddress

        self._thisCompass = 0
        self._thisAccelerometer = []
        self._thisGPS = []
        self._thisGyro = []

        self._lastCompass = 0
        self._lastAccelerometer = []
        self._lastGPS = []
        self._lastGyro = []

        self._host = ''
        self._port = 5555
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._s.bind((self._host, self._port))

    def refreshData(self):
        try:
            self._message, self._address = s.recvfrom(8192)
            self._data = self._message.split( "," )
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            traceback.print_exc()

    def get_compass(self):

    def get_accelerometer(self):
        self._thisAccelerometer = [self._data[2], self._data[3], self._data[4]]
        return self._thisAccelerometer

    def get_gps(self):

    def get_gyro(self):

    def get_changeCompass(self):

    def get_changeAccelerometer(self):
        self._lastAccelerometer = self._thisAccelerometer
        self._thisAccelerometer = [self._data[2], self._data[3], self._data[4]]
        return [self._lastAccelerometer[0]-self._thisAccelerometer[0], self._lastAccelerometer[1]-self._thisAccelerometer[1], self._lastAccelerometer[2]-self._thisAccelerometer[2]]

    def printStream(self):
        print str(self._data)
