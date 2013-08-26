#! /usr/bin/env python

from psfile import EPSFile

fd = EPSFile("ex2.eps", 100, 100)
fd.append("""
  % outer square
  0 0 moveto
  100 0 lineto
  100 100 lineto
  0 100 lineto
  closepath

  % inner square, open to the left
  10 10 moveto
  90 10 lineto
  90 90 lineto
  10 90 lineto

  % draw the constructed path
  stroke
""")
fd.close()
