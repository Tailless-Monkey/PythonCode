#!/usr/bin/env python
# coding=utf-8
from PIL import Image

ascii_char = list(r"$&%B#=-. ")

def select_ascii_char(r, g, b):
    gray = int((19595 * r + 38469 * g + 7472 *b) >>16)
    unit = 256.0/len(ascii_char)
    return ascii_char[int(gray/unit)]

def output(imgpath, width=100, height=100):
    im = Image.open(imgpath)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""

    for h in xrange(height):
        for w in xrange(width):
            txt += select_ascii_char(*im.getpixel((w,h))[:3])
        txt += '\n'
    return 
