MinION runs generate a nice Final Report that contains valuable run data - I'm including an example of the file name format and a screenshot below:\
"MinKNOW Run Report-28-11-2023-FAX33213.pdf"
<img width="719" alt="image" src="https://github.com/acread/utilities/assets/43852873/1416d080-b289-4a4b-8108-0c12f62bcd8a">

Sometimes this report is unavailable or needs to be regenerated - I'm using NanoR for this \
https://davidebolo1993.github.io/nanordoc/

Here is an example for the PromethION data that Chris Faulk ran for us:
`````R
devtools::install_github("davidebolo1993/NanoR")
library(NanoR)

setwd("/Users/read0094/Desktop/Wheat")

summary=file.path("/Users/read0094/Desktop/Wheat/sequencing_summary_PAQ23751_5a9da8f8_b0478d44.txt")

#Generate a simple text summary file
out1<-file.path("report_1.NanoR.tsv")
NanoR::report(summary=summary, out=out1) #or report(summary=summary1, out=out1)

#Generate a nice interactive visualization of output over time
out2<-file.path("yield_1.NanoR.html")
NanoR::yield(summary=summary, time=1, out=out2) #time can be adjusted to different hour fractions
`````

Here's what some of the output looks like: 
<img width="1000" alt="image" src="https://github.com/acread/utilities/assets/43852873/a9161518-d5de-40bf-b174-38ff91516f6c">
