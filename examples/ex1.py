#! /usr/bin/env python

from random import uniform
from psfile import EPSFile

fd = EPSFile("ex1.eps", 600, 100)

# dark gray background
fd.append("0.1 setgray")
fd.append("0 0 %d %d rectfill"%(fd.width, fd.height))

# a grid of dark orange lines
fd.append("1 .596 .118 setrgbcolor")
fd.append("1 setlinewidth")
for i in range(1,5):
    y = 100*i/5.0
    fd.append("5 %.1f moveto 595 %.1f lineto"%(y,y))
for i in range(1,30):
    x = 100*i/5.0
    fd.append("%.1f 5 moveto %.1f 95 lineto"%(x,x))
fd.append("stroke")

# randomly colored, filled squares
for i in range(0,30):
    x = i*20+3
    for j in range(0,5):
        y = j*20+3
        col = uniform(0,1)
        if 31*uniform(0,1) > i+1:
            fd.append("0 %.3f 0 setrgbcolor"%col)
        else:
            fd.append("%.3f 0 0 setrgbcolor"%col)
        fd.append("%.1f %.1f 14 14 rectfill"%(x,y))

fd.close()
