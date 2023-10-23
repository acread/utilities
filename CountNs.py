#I pulled this from https://gist.github.com/idolawoye/b8846f4f1e12f9e82a924e9a7bf2ae8e

#!/usr/bin/env python

from Bio import SeqIO

fasta = "the_fasta_file.fasta"

for record in SeqIO.parse(fasta, "fasta"):
  print("ID: %s" % record.id)
  print("Sequence length: %s" % len(record))
  print("Number of Ns: %s" % record.seq.count('N'))
  print((record.seq.count('N')/len(record))*100)
