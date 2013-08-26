#! /usr/bin/env python

from __future__ import division

from random import uniform
from psfile import EPSFile

cols = 7
rows = 4
gap = 3

fd = EPSFile("ex4.eps", 350, 80)
fd.append("/Times-Roman findfont 8 scalefont setfont")
dx = (fd.width+gap)/cols
dy = (fd.height+gap)/rows
w = dx - gap
h = dy - gap
for j in range(0, rows):
    for i in range(0, cols):
        r = g = b = 0
        while r + g + b < 1:
            r, g, b = [ uniform(0,1), uniform(0,1), uniform(0,1) ]
        fd.append("%.1f %.1f %.1f setrgbcolor"%(r,g,b))
        fd.append("%f %f %f %f rectfill"%(i*dx, j*dy, w, h))
        fd.append("0 setgray")
        fd.append("%f %f moveto"%(i*dx+4, j*dy+3))
        fd.append("(%.1f, %.1f, %.1f) show"%(r,g,b))
fd.close()
