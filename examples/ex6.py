#! /usr/bin/env python

from psfile import EPSFile

fonts = [
    "Times-Roman", "Times-Italic", "Times-Bold", "Times-BoldItalic",
    "Helvetica", "Helvetica-Oblique", "Helvetica-Bold",
    "Helvetica-BoldOblique", "Courier", "Courier-Oblique",
    "Courier-Bold", "Courier-BoldOblique", "Symbol"
]
str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

fd = EPSFile("ex6.eps", 420, len(fonts)*12)
for i, name in enumerate(reversed(fonts)):
    fd.append("/TimesRoman findfont 10 scalefont setfont")
    fd.append("0 %d moveto"%(12*i+3))
    fd.append("(%s:) show"%name)
    fd.append("/%s findfont 10 scalefont setfont"%name)
    fd.append("100 %d moveto"%(12*i+3))
    fd.append("(%s) show"%str)
fd.close()
