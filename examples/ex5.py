#! /usr/bin/env python

from psfile import EPSFile

fd = EPSFile("ex5.eps", 350, 50)
# draw the yellow background
fd.append("1 1 0 setrgbcolor")
fd.append("0 0 %d %d rectfill"%(fd.width, fd.height))
# draw black circles filled with red
fd.append("0 setgray")
for x in range(25, 375, 50):
    fd.append("""%f 25 20 0 360 arc
                 gsave
                 1 0 0 setrgbcolor
                 fill
                 grestore
                 stroke"""%x)
fd.close()
