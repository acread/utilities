This is a little utility script to extract CG, CHG, and CHH sites from a fasta (genome)
It can also be used to look for other motifs...
As input you point to your .fa of interest and tell it the motif that you want to find.  
The output is trimmed to give you 5 columns that look like this:

````
seqID	patternName	strand	start	end
Chr01	CG	+	25	26
Chr01	CG	+	30	31
Chr01	CG	+	34	35
Chr01	CG	+	42	43
Chr01	CG	+	89	90
Chr01	CG	+	122	123
Chr01	CG	+	135	136
Chr01	CG	+	137	138
Chr01	CG	+	191	192
````

````
#!/bin/bash -l
#SBATCH --time=4:00:00
#SBATCH --ntasks=1
#SBATCH --mem=40g
#SBATCH --tmp=8g
#SBATCH --job-name=mC motif finder
#SBATCH --mail-type=ALL
#SBATCH --mail-user=read0094@umn.edu

### First create a conda environment 'conda create --name seqkit'
### Activate the environment 
conda activate seqkit

### Install seqkit into the environment 'conda install -c bioconda seqkit'
### Seqkit tools are now available when you activate the environment

### I'm basing this on Pete Crisp's script - but my version will need to be modified for each genome/output
#CG
#outputFile="${faname%%.*}_CG.txt"
#cat $fa | seqkit locate -i -p "CG" | cut -f 1-2,4-6 > sites_files/$outputFile

cat /home/springer/read0094/SetariaStuff/Sviridis_500_v2.0.fa | seqkit locate -i -p "CG" | cut -f 1-2,4-6 > Sviridis_500_v2.0_CG.txt

#D is the degenerate nucleotide code for 'not C'
#note that the -d flag must be used to indicate the presence of a degenerate base in the motif
cat /home/springer/read0094/SetariaStuff/Sviridis_500_v2.0.fa | seqkit locate -i -d -p "CDG" | cut -f 1-2,4-6 > Sviridis_500_v2.0_CHG.txt

cat /home/springer/read0094/SetariaStuff/Sviridis_500_v2.0.fa | seqkit locate -i -d -p "CDD" | cut -f 1-2,4-6 > Sviridis_500_v2.0_CHH.txt

````
