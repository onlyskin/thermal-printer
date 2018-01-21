import serial

from printer import Printer, PrinterSettings

if __name__ == '__main__':
    port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

    printer = Printer(port)
    printer_settings = PrinterSettings(port)

    printer_settings.set_big_chars()
    printer.print_kanji(u'亜唖娃阿哀愛\n')
    printer_settings.unset_big_chars()
    printer.print_text('test\n')
    printer.print_space()
