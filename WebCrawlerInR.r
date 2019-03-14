install.packages("XML")
library(XML)
mps = "http://news.bbc.co.uk/2/hi/uk_politics/8044207.stm"

mps.doc<-htmlParse(mps)

mps.tabs<-readHTMLTable(mps.doc)

web_data<-as.data.frame(mps.tabs[3])
web_data<-web_data[3:651,]
web_data<-web_data[1:646,]
