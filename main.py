# -*- coding: utf-8

from printer import Printer, PrinterSettings
from port_wrapper import PortWrapper

if __name__ == '__main__':
    port = PortWrapper()
    printer = Printer(port)
    printer_settings = PrinterSettings(port)

    printer_settings.set_big_chars()
    printer.print_kanji(u'亜唖娃阿哀愛\n')
    printer_settings.unset_big_chars()
    printer.print_text('test\n')
    printer.print_space()
