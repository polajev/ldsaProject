# This code prints out all of the lines from a CRAM file, in plain text form. 

import pysam
cramfile = pysam.AlignmentFile("HG00096.cram", "rc")
for read in cramfile.fetch():
	print(read)
	
cramfile.close()