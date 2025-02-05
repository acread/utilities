

### To move batches of files into subdirectories.... as written 25 files get moved

````
 n=0; for f in *; do d="dir$((n++ / 25))"; mkdir -p "$d"; mv -- "$f" "$d/$f"; done
````


### To get chromosome lengths from a fasta

````
cat file.fa | awk '$0 ~ ">" {if (NR > 1) {print c;} c=0;printf substr($0,2,100) "\t"; } $0 !~ ">" {c+=length($0);} END { print c; }'
````

### To split a multi-fasta into individual fastas
`````
cat /home/springer/shared/ns-genome/Zmays_W22/10.fasta |awk '/^>/ {if(N>0) printf("\n"); printf("%s\n",$0);++N;next;} { printf("%s",$0);} END {printf("\n");}' |split -l 2 --additional-suffix=.fasta - seq_
`````

### To subsample from a fastq - from tommy.tang.bsky.social
`````
cat file.fq | paste - - - - | awk 'BEGIN{srand(1234)}{if(rand() < 0.01) print $0}' | tr '\t' '\n' > out.fq
#What’s happening? The srand(1234) ensures reproducibility (same random seed every time). The rand() function generates a random number, and if it’s < 0.01, the read is included.

#Second approach: Using shuf for random sampling:
#Here, shuf randomly selects 1000 reads from the input file and outputs them.
cat file.fq | paste - - - - | shuf -n 1000 | tr '\t' '\n' > out.fq
`````
