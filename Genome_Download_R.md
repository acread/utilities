Downloading genomes is still more challenging than I think it should be -- here's one way to do it with R \
First we check to make sure our genome of interest is available, then we point to the appropriate db and download \
Note that the download will appear in a new folder with a name like "_ncbi_downloads"

`````R
# Install package dependencies
#BiocManager::install("Biostrings")
#BiocManager::install("biomaRt")
#BiocManager::install("ropensci/biomartr")

library("Biostrings")
library("biomaRt")
library("biomartr")
library("tidyverse")
# import genome as Biostrings object
options(timeout = 30000)

is.genome.available(
  db = "genbank",
  organism="GCA_900519105.1",
  #skip_bacteria = "TRUE",
  details = FALSE
)

#for ensemble use refseq
Wheatv2 <- getGenome(
  db       = "refseq",
  organism = "GCF_018294505.1") %>%
  read_genome()

Wheatv2_gff <- getGFF(
  db       = "refseq",
  organism = "GCF_018294505.1") %>%
  read_gff()

#for NCBI use genbank
Wheatv1 <- getGenome(
  db = "genbank",
  organism = "GCA_900519105.1") %>%
  read_genome()
`````
