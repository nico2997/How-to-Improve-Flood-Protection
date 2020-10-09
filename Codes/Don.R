library(readxl)
DonData <- read_xlsx("Don data.xlsx") # Importing data set
day <- DonData$Day
flowrate <- DonData$Flowrate
height <- DonData$Riverheight

### Create vectors for each variable ###
dayvector <- c(day)
flowvector <- c(flowrate)
heightvector <- c(height)

### Create function to scale data to between 0 and 1 ###
scalevector <- function(x) {
  return ((x - min(x)) / (max(x) - min(x)))
}

### Create vectors for each variable with scaled data ###
scaledday <- scalevector(dayvector)
scaledflow <- scalevector(flowvector)
scaledheight <- scalevector(heightvector)

### Combine scaled vectors to allow one graph ###
negativeheight <- -(scaledheight)
heightandday <- c(negativeheight, scaledday, negativeheight)
twoflow <- c(scaledflow, scaledflow)
negativeday <- -(scaledday)
flowandday <- c(negativeday, twoflow)

### Scale values of straight lines ###
scaledht <- (2.9 - min(height)) / (max(height) - min(height))
scaledhm <- (4.06 - min(height)) / (max(height) - min(height))
scaledqm <- (225.9 - min(flowrate)) / (max(flowrate) - min(flowrate))
scaledqt <- (164.1 - min(flowrate)) / (max(flowrate) - min(flowrate))

### Plot graph and straight lines ###
plot(heightandday, flowandday, pch=".", axes=FALSE, xlab=NA, ylab=NA, xaxt='n', yaxt='n', main="Don graph")
axis(side=1, cex.axis=0.5, pos=0, at=c(-(4481/4156),-(3481/4156),-(2481/4156),-(1481/4156),-(481/4156),1/4,2/4,3/4,1),labels=c("5","4","3","2","1","26","27","28","29"))
axis(side=2,cex.axis=0.5, pos=0, at=c(-1,-3/4,-2/4,-1/4,1024/6249,758/2083,3524/6249,4774/6249,2008/2083,1.164026244),labels=c("29","28","27","26","50","100","150","200","250","300"), las=1)
polygon(x=scaledday[49:104], y=scaledflow[49:104], col="grey")
abline(v=-(scaledht), lty=3)
abline(v=-(scaledhm), lty=3)
abline(h=scaledqm, lty=3)
abline(h=scaledqt, lty=3)
segments(x0=0, y0=0, x1 = -max(scaledheight), y1 = max(scaledflow), lty=2)
segments(x0=scaledday[49], y0=scaledqt, x1=scaledday[104], y1=scaledqt)
segments(x0=scaledday[49], y0=scaledqm, x1=scaledday[104], y1=scaledqm)
segments(x0=scaledday[49], y0=scaledqt, x1=scaledday[49], y1=scaledqm)
segments(x0=scaledday[104], y0=scaledqt, x1=scaledday[104], y1=scaledqm)
segments(x0=scaledday[49], y0=-0.35, x1=scaledday[49], y1=scaledqt, lty=3)
segments(x0=scaledday[104], y0=-0.35, x1=scaledday[104], y1=scaledqt, lty=3)
arrows(x0=scaledday[49], y0=-0.35, x1=scaledday[104], y1=-0.35, length = 0.05, code=3)

### Axes and line labels ###
text(x=0, y=-1 ,label="t", cex=0.5, pos=4, font=3)
text(x=0.03, y=-1 ,label="[day]", cex=0.5, pos=4)
text(x=0, y=1 ,label="Q", cex=0.5, pos=4, font=3)
text(x=0.135, y=1 ,label=expression("[m"^3), cex=0.5)
text(x=0.125, y=0.99 ,label="/s]", cex=0.5, pos=4)
text(x=0.93, y=-0.05 ,label="t", cex=0.5, pos=1, font=3)
text(x=1, y=-0.05 ,label="[day]", cex=0.5, pos=1)
text(x=-0.98, y=-0.01 ,label=bquote(bar(h)), cex=0.5, pos=3, font=3)
text(x=-0.92, y=-0.01 ,label="[m]", cex=0.5, pos=3)
text(x=-(scaledht), y=-1 ,label="hT", cex=0.5, pos=4, font=3)
text(x=-(scaledhm), y=-1 ,label="hM", cex=0.5, pos=4, font=3)
text(x=1, y=scaledqm ,label="Qm", cex=0.5, pos=1, font=3)
text(x=1, y=scaledqt ,label="Qt", cex=0.5, pos=1, font=3)
text(x=scaledday[148], y=-0.35, label="Tf", cex=0.5, pos=1, font=3)
text(x=scaledday[330], y=-0.55, label="FEV ??? 3.00Mm^3", cex=0.5)
text(x=scaledday[345], y=-0.62, label="Tf = 13.50hrs", cex=0.5)
text(x=scaledday[350], y=-0.69, label="hT = 2.90m", cex=0.5)
text(x=scaledday[350], y=-0.76, label="hM = 4.06m", cex=0.5)
text(x=scaledday[320], y=-0.83, label="Qt = 164.1", cex=0.5)
text(x=scaledday[370], y=-0.82 ,label=expression("m"^3), cex=0.5)
text(x=scaledday[385], y=-0.82 ,label="/s", cex=0.5)
text(x=scaledday[320], y=-0.9, label="Qm = 225.9", cex=0.5)
text(x=scaledday[370], y=-0.89 ,label=expression("m"^3), cex=0.5)
text(x=scaledday[385], y=-0.89,label="/s", cex=0.5)
