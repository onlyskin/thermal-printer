# -*- coding: utf-8

import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)

def set_left_justify():
    port.write('\x1b')
    port.write('\x61')
    port.write('\x00')

text = u'''亜唖娃阿哀愛挨逢葵茜悪握渥旭葦芦鯵梓圧斡扱宛姐飴絢綾鮎或粟袷安庵按暗案闇鞍杏以伊位依偉囲夷委威尉惟意慰易椅為畏異移維緯胃萎衣謂違遺医井亥域育郁磯一壱溢逸稲茨芋鰯允印咽員因姻引飲淫胤蔭院陰隠韻吋右宇烏羽'''.encode('gbk')

def set_big_chars():
    port.write('\x1d')
    port.write('\x21')
    port.write(chr(2|16))

def unset_big_chars():
    port.write('\x1d')
    port.write('\x21')
    port.write(chr(0))

def set_kanji_mode():
    port.write('\x1c')
    port.write('\x26')

def write_newlines():
    port.write('\x00\x0a')
    port.write('\x00\x0a')
    port.write('\x00\x0a')

if __name__ == '__main__':
    unset_big_chars()
    port.write(text)
    write_newlines()
