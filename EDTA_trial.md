
## Installation and first run

A small group of Springer/Hirsch people are working to learn the ins and outs of EDTA \
https://github.com/oushujun/EDTA 

I did the installation of a conda environment on MSI 

A batch script to try EDTA \
I'm using a genome fasta from my 'SetaraStuff' folder - it does not include unplaced contigs or plastid DNA

`````
#!/bin/bash -l
#SBATCH --time=48:00:00
#SBATCH --ntasks=4
#SBATCH --mem=32g
#SBATCH --tmp=10g
#SBATCH --job-name=EDTA
#SBATCH --mail-type=ALL
#SBATCH --mail-user=read0094@umn.edu

conda activate EDTA

cd /home/springer/read0094/SetariaStuff/EDTA_trials

perl /home/springer/read0094/Software/EDTA/EDTA.pl --genome /home/springer/read0094/SetariaStuff/ME034_v0.4.Chr1_9.fa \
--overwrite 1 --sensitive 1 --anno 1 --evaluate 1 --threads 10
`````

This ran for 48 hours and completed many of the first steps, but did not run to completion (did not finish the \
homology based analysis)

`````

########################################################
##### Extensive de-novo TE Annotator (EDTA) v1.9.9  ####
##### Shujun Ou (shujun.ou.1@gmail.com)             ####
########################################################



Fri Nov 19 15:46:10 CST 2021    Dependency checking:
                                All passed!

Fri Nov 19 15:46:25 CST 2021    Obtain raw TE libraries using various structure-based programs:
Fri Nov 19 15:46:25 CST 2021    EDTA_raw: Check dependencies, prepare working directories.

Fri Nov 19 15:46:32 CST 2021    Start to find LTR candidates.

Fri Nov 19 15:46:32 CST 2021    Identify LTR retrotransposon candidates from scratch.

Fri Nov 19 16:36:28 CST 2021    Finish finding LTR candidates.

Fri Nov 19 16:36:28 CST 2021    Start to find TIR candidates.

Fri Nov 19 16:36:28 CST 2021    Identify TIR candidates from scratch.

Species: others
Fri Nov 19 22:10:00 CST 2021    Finish finding TIR candidates.

Fri Nov 19 22:10:00 CST 2021    Start to find Helitron candidates.

Fri Nov 19 22:10:00 CST 2021    Identify Helitron candidates from scratch.

Sat Nov 20 02:06:49 CST 2021    Finish finding Helitron candidates.

Sat Nov 20 02:06:49 CST 2021    Execution of EDTA_raw.pl is finished!

Sat Nov 20 02:06:50 CST 2021    Obtain raw TE libraries finished.
                                All intact TEs found by EDTA:
                                        ME034_v0.4.Chr1_9.fa.mod.EDTA.intact.fa
                                        ME034_v0.4.Chr1_9.fa.mod.EDTA.intact.gff3

Sat Nov 20 02:06:50 CST 2021    Perform EDTA advance filtering for raw TE candidates and generate the stage 1 library:

Sat Nov 20 03:53:27 CST 2021    EDTA advance filtering finished.

Sat Nov 20 03:53:27 CST 2021    Perform EDTA final steps to generate a non-redundant comprehensive TE library:

                                Use RepeatModeler to identify any remaining TEs that are missed by structure-based methods.

slurmstepd: error: *** JOB 8467544 ON cn0234 CANCELLED AT 2021-11-21T15:46:02 DUE TO TIME LIMIT ***
`````

I'm not sure if I can re-start from here, or need to re-run the entire pipeline with more resources \
here are the files that were generated:

`````
(base) read0094@ln0006 [~/SetariaStuff/EDTA_trials] % ls -lh
total 434M
lrwxrwxrwx. 1 read0094 springer   57 Nov 19 15:46 ME034_v0.4.Chr1_9.fa -> /home/springer/read0094/SetariaStuff/ME034_v0.4.Chr1_9.fa
-rw-------. 1 read0094 springer 383M Nov 19 15:46 ME034_v0.4.Chr1_9.fa.mod
drwx------. 2 read0094 springer  24K Nov 20 03:53 ME034_v0.4.Chr1_9.fa.mod.EDTA.combine
drwx------. 3 read0094 springer 4.0K Nov 20 06:02 ME034_v0.4.Chr1_9.fa.mod.EDTA.final
-rw-------. 1 read0094 springer 2.0M Nov 20 02:06 ME034_v0.4.Chr1_9.fa.mod.EDTA.intact.gff3
drwx------. 5 read0094 springer 4.0K Nov 20 02:06 ME034_v0.4.Chr1_9.fa.mod.EDTA.raw
-rw-------. 1 read0094 springer 1.8K Nov 21 15:46 slurm-8467544.out
`````
### Tip from Zhikai 
Zhikai suggests breaking the genome into separate chromosomes and running EDTA on each chromosome to save time (I like this)

I am trying to pick up where things left off - based on Shujun's documentation I am trying this:
`````
#!/bin/bash -l
#SBATCH --time=48:00:00
#SBATCH --ntasks=4
#SBATCH --mem=32g
#SBATCH --tmp=10g
#SBATCH --job-name=EDTA_final
#SBATCH --mail-type=ALL
#SBATCH --mail-user=read0094@umn.edu

conda activate EDTA

cd /home/springer/read0094/SetariaStuff/EDTA_trials

#modified so that overwrite = 0 and step = final
perl /home/springer/read0094/Software/EDTA/EDTA.pl --genome /home/springer/read0094/SetariaStuff/ME034_v0.4.Chr1_9.fa \
--overwrite 0 --step final --sensitive 1 --anno 1 --evaluate 1 --threads 10
`````

## Quick dirty analysis of output

9,016 structural elements were identified -- NOTE that this includes some redundancy (for example target site duplications \
are included with LTR elements) 

6,622 elements remain after I get rid of long_terminal_repeat and target_site_duplication (6,622 does include 600 'repeat_region's \
I'm not sure how these are defined or if they should be included)

A quick look at the RNA and DNA elements is a little bit surprising to me (see image) - there are many more DNA elements.  This may be due \
to the strict requirements of the structural annotation.  For some analyses this makes sense (for example, when we were looking \
for potentially active TEs.... however we do not catch a COPIA element that the ME034V paper makes a big deal about as a new \
insertion in ME034V relative to A10.  I'm not sure how to feel about this).

`````
Copia_LTR_retrotransposon	291
Gypsy_LTR_retrotransposon	231
LTR_retrotransposon	78
hAT_TIR_transposon	431
CACTA_TIR_transposon	1126
Mutator_TIR_transposon	805
Tc1_Mariner_TIR_transposon	1511
PIF_Harbinger_TIR_transposon	820
helitron	729
repeat_region	600
	6622
`````
