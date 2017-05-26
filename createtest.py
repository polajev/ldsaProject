import pysam
cramfile = pysam.AlignmentFile("HG00096.cram", "rc")

newfile = pysam.AlignmentFile("test.cram", "wc", template=cramfile)
for read in cramfile.fetch():
    newfile.write(read)

newfile.close()
cramfile.close()