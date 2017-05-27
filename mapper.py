#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	list = line.split()
	gcount=list[9].count('G')
	ccount=list[9].count('C')
	gccount=gcount+ccount
	total=list[9].count('')-1
	print(gccount, total)

