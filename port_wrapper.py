import serial

class PortWrapper():
    def __init__(self):
        self._port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

    def write(self, *args):
        self._port.write(*args)
