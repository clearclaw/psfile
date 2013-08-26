#! /usr/bin/env python

from __future__ import division

from math import pow
from psfile import EPSFile

min_lw = .5
max_lw = 9
steps = 18

fd = EPSFile("ex3.eps", 350, 38,
             margin_left=10+.5*min_lw, margin_right=10+.5*max_lw)
fd.append("/Times-Roman findfont 10 scalefont setfont")
for i in range(0, steps+1):
    lw = min_lw * pow(max_lw/min_lw, i/steps)
    x = fd.width*i/steps
    fd.append("%.1f setlinewidth"%lw)
    fd.append("%f 0 moveto 0 27 rlineto"%x)
    fd.append("stroke")
    fd.append("%f 30 moveto"%(x-6))
    fd.append("(%.1f) show"%lw)
fd.close()
