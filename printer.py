# -*- coding: utf-8
import serial

class PrinterSettings():
    def __init__(self, port):
        self.port = port

    def _write_bytes(self, *bytes):
        for b in bytes:
            self.port.write(b)

    def set_left_justify(self):
        self._write_bytes('\x1b', '\x61', '\x00')
    
    def set_big_chars(self):
        self._write_bytes('\x1d', '\x21', chr(2|16))
    
    def unset_big_chars(self):
        self._write_bytes('\x1d', '\x21', chr(0))
    
    def set_kanji_mode(self):
        self._write_bytes('\x1c', '\x26')
    
class Printer():
    def __init__(self, port):
        self.port = port

    def print_text(self, text):
        self.port.write(text)

    def print_kanji(self, text):
        self.port.write(text.encode('gbk'))

    def print_space(self):
        self.port.write('\x00\x0a')
        self.port.write('\x00\x0a')
        self.port.write('\x00\x0a')
        
if __name__ == '__main__':
    port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

    printer = Printer(port)
    printer_settings = PrinterSettings(port)

    printer_settings.set_big_chars()
    printer.print_kanji(u'亜唖娃阿哀愛\n')
    printer_settings.unset_big_chars()
    printer.print_text('test\n')
    printer.print_space()
