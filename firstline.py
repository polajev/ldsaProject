import pysam
cramfile = pysam.AlignmentFile("HG00096.cram", "rc")
iterator=cramfile.fetch()
print(next(iterator))

cramfile.close()