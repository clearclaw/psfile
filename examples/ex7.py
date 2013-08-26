#! /usr/bin/env python

from __future__ import division

from math import pi, sqrt
from random import vonmisesvariate
from psfile import EPSFile

# a sample from a von Mises distribution
sample = [ vonmisesvariate(pi/4, 1.0) for i in range(0,200) ]

# generate a histogram of the data
nhist = 4 * int(sqrt(len(sample))/4 + 0.5);
count = [ 0 ] * nhist
for x in sample:
    y = x/(2*pi) % 1
    count[int(y*nhist+.5)%nhist] += 1

# turn into a plot
radius = 72
fd = EPSFile("ex7.eps", 4*radius, 4*radius)
fd.append("/Times-Roman findfont 10 scalefont setfont")
fd.append("%f %f translate"%(2*radius, 2*radius))
fd.append("%f setlinewidth"%((2*pi*radius) / nhist - 1))
for k in count:
    r = radius * (1 + .9*k/max(count))
    fd.append("0 0 moveto %f 0 lineto"%r)
    fd.append("%f -3 moveto (%d) show"%(r+3, k))
    fd.append("%f rotate"%(360/nhist))
fd.append("stroke")
fd.append("""1 setlinewidth
             0 0 %f 0 360 arc
             gsave 1 setgray fill grestore stroke"""%radius)
fd.append("/Symbol findfont 24 scalefont setfont")
fd.append("-35 -10 moveto (k = 1.0) show")
fd.close()
