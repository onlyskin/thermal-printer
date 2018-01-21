class Printer():
    def __init__(self, port):
        self._port = port

    def print_text(self, text):
        self._port.write(text)

    def print_kanji(self, text):
        self._port.write(text.encode('gbk'))

    def print_space(self):
        self._port.write('\x00\x0a')
        self._port.write('\x00\x0a')
        self._port.write('\x00\x0a')

class PrinterSettings():
    def __init__(self, port):
        self._port = port

    def _write_bytes(self, *bytes):
        for b in bytes:
            self._port.write(b)

    def set_left_justify(self):
        self._write_bytes('\x1b', '\x61', '\x00')
    
    def set_big_chars(self):
        self._write_bytes('\x1d', '\x21', chr(2|16))
    
    def unset_big_chars(self):
        self._write_bytes('\x1d', '\x21', chr(0))
    
    def set_kanji_mode(self):
        self._write_bytes('\x1c', '\x26')
