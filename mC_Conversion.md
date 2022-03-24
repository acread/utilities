

I'm pulling the chloroplast data from the BSMAP.out.txt files to calculate the conversion rate for each run

grep "CP" PHJ01_S1_BSMAP_out.txt > CP_PHJ01_S1_BSMAP_out.txt
grep "CP" PHJ02_S2_BSMAP_out.txt > CP_PHJ02_S2_BSMAP_out.txt
grep "CP" PHJ03_S3_BSMAP_out.txt > CP_PHJ03_S3_BSMAP_out.txt
grep "CP" PHJ04_S4_BSMAP_out.txt > CP_PHJ04_S4_BSMAP_out.txt
grep "CP" PHJ05_S5_BSMAP_out.txt > CP_PHJ05_S5_BSMAP_out.txt
grep "CP" PHJ06_S6_BSMAP_out.txt > CP_PHJ06_S6_BSMAP_out.txt
grep "CP" PHJ07_S7_BSMAP_out.txt > CP_PHJ07_S7_BSMAP_out.txt

Here's how Pete did it - as far as I can tell he is just using CHH sites:

````
awk -F$"\\t" \
'BEGIN {OFS = FS} {if($1=="Pt" && $5=="CHH") print}' \
BSMAPratio/${ID}_BSMAP_out.txt | \
awk '{sum1 += $9; sum2 +=$8} END {print sum1, sum2 , 100-((sum2/sum1)*100)}' > ConversionRate/${ID}_conversion_rate.txt
# conversion rate pete - using eff_CT
awk -F$"\\t" \
'BEGIN {OFS = FS} {if($1=="Pt" && $5=="CHH") print}' \
 BSMAPratio/${ID}_BSMAP_out.txt | \
 awk '{sum1 += $7; sum2 +=$8} END {print sum1, sum2 , 100-((sum2/sum1)*100)}' > ConversionRate/${ID}_conversion_rate_eff_C.txt
 ````
 
 I'm going to try to replicate this in R...
Note, I don't seem to have the PHJ07_S7_BSMAP_out.txt file... not sure what's going on here, may have to repeat the analysis
### I was able to get PHJ07 to run during the resubmission to TPJ - data added below

````R
setwd("/Users/read0094/Desktop/SetariaStuff_Assorted/ConversionRate/")

PHJ01=read.table("CP_PHJ01_S1_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ02=read.table("CP_PHJ02_S2_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ03=read.table("CP_PHJ03_S3_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ04=read.table("CP_PHJ04_S4_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ05=read.table("CP_PHJ05_S5_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ06=read.table("CP_PHJ06_S6_BSMAP_out.txt", header=FALSE, sep="\t")
PHJ07=read.table("CP_PHJ07_S7_BSMAP_out.txt", header=FALSE, sep="\t")

#Now just grab CHH sites
PHJ01_CHH=subset(PHJ01, V5=="CHH")
PHJ02_CHH=subset(PHJ02, V5=="CHH")
PHJ03_CHH=subset(PHJ03, V5=="CHH")
PHJ04_CHH=subset(PHJ04, V5=="CHH")
PHJ05_CHH=subset(PHJ05, V5=="CHH")
PHJ06_CHH=subset(PHJ06, V5=="CHH")
PHJ07_CHH=subset(PHJ07, V5=="CHH")

#Conversion Rate
PHJ01_Conv=100-(((sum(PHJ01$V8)/sum(PHJ01$V7))*100))
PHJ02_Conv=100-(((sum(PHJ02$V8)/sum(PHJ02$V7))*100))
PHJ03_Conv=100-(((sum(PHJ03$V8)/sum(PHJ03$V7))*100))
PHJ04_Conv=100-(((sum(PHJ04$V8)/sum(PHJ04$V7))*100))
PHJ05_Conv=100-(((sum(PHJ05$V8)/sum(PHJ05$V7))*100))
PHJ06_Conv=100-(((sum(PHJ06$V8)/sum(PHJ06$V7))*100))
PHJ07_Conv=100-(((sum(PHJ07$V8)/sum(PHJ07$V7))*100))

> PHJ01_Conv
[1] 99.62594
> PHJ02_Conv
[1] 99.76784
> PHJ03_Conv
[1] 99.8132
> PHJ04_Conv
[1] 99.77699
> PHJ05_Conv
[1] 99.42762
> PHJ06_Conv
[1] 99.57129
> PHJ07_Conv
[1] 99.80
````
