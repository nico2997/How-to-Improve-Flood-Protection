library(readxl)
Windsor <- read_xlsx("Thames data.xlsx", 
                      sheet = "Sheet3") # Importing data set

DW=Windsor$Day # Setting data names
FlW=Windsor$Flow
StW=Windsor$Stage

minDW=1 # Setting min and max for Day data
maxDW=39
minFlW=30 # Setting min and max for Flow data
maxFlW=360
minStW=3 # Setting min and max for Stage data
maxStW=6

htW=4.8
QtW=300
# 300 given by [23]
# Checked by looking at given data to find an approx. value; raw data given use of ultrasound [24]


DW_sc=(DW-minDW)/(maxDW-minDW) # Scaling the data sets; [9].
FlW_sc=(FlW-minFlW)/(maxFlW-minFlW)
StW_sc=(StW-minStW)/(maxStW-minStW)

# Scaling ht, Qt - as well as, stating scaled vectors needed for polygon
htW_sc=(htW-minStW)/(maxStW-minStW)
QmaxW_sc=(max(FlW)-minFlW)/(maxFlW-minFlW)
QtW_sc=(QtW-minFlW)/(maxFlW-minFlW)

# Notified of which function by supervisor [8]. 
# Looked at RStudio help section for structure.
ScVecQW=FlW_sc[which(FlW>QtW)]
ScVecDW=DW_sc[which(FlW>QtW)]
lSVD=length(ScVecDW)

# FEV Calculation
deltk=900 # 15 minutes in seconds [8].
QWk=FlW[which(FlW>QtW)]
FEV=sum(QWk-QtW)*deltk

plot(0,0, type="l", axes=F, xlim=cbind(-1.1,1.1), ylim=cbind(-1.1,1.1), xlab="", ylab="", main="Quadrant plot for the Datchet 2014 flood") 
# creating an empty plot [7, p.104-5][10]

lines(x=DW_sc, y=FlW_sc, type="l") #[7, p.104-5]
lines(x=-StW_sc, y=FlW_sc, type="l")
lines(x=-StW_sc, y=-DW_sc, type="l")

# Notified of segments function by fellow project member [11]. 
# Looked at RStudio help section for structure.
segments(-htW_sc, QtW_sc, 1, QtW_sc, lty=3) 
segments(-htW_sc, -1, -htW_sc, QtW_sc, lty=3)

segments(ScVecDW[1], -0.25, ScVecDW[1], QmaxW_sc, lty=3)
segments(ScVecDW[lSVD], -0.25, ScVecDW[lSVD], QmaxW_sc, lty=3)
segments(-min(StW_sc), min(FlW_sc), -max(StW_sc), max(FlW_sc), lty=2) 

# Adding the double-ended arrow 
# Notified of arrows function by [13, p. 79]
arrows(ScVecDW[1], -0.1875, ScVecDW[lSVD], -0.1875, length=0.05)
arrows(ScVecDW[lSVD], -0.1875, ScVecDW[1], -0.1875, length=0.05) 

# [12 p.50-58] [11]
polygon(cbind(ScVecDW[1], ScVecDW, ScVecDW[lSVD]), cbind(QtW_sc, ScVecQW, QtW_sc), col="light blue")

segments(ScVecDW[1], QtW_sc, ScVecDW[lSVD], QtW_sc, lty=1, lwd=2) 

axis(1, at=NULL, labels = FALSE, tick = TRUE, pos = 0,0, lwd.ticks=0, lwd=2)
# Adding axis. Found function via RStudio help section
axis(2, at=NULL, labels = FALSE, tick = TRUE, pos = 0,0, lwd.ticks=0, lwd=2)

# Notified of mtext function by [7, p.105].
# Looked at RStudio help section
mtext("Day", 1) # Adding axis labels
mtext("Height [m]", 2, las=1)
mtext("Day", 4, las=1)

# Notified of text function by [7, p.105]. Looked at RStudio help section
text(cbind(0,0.3333333,0.6666667,1), cbind(-0.05,-0.05,-0.05,-0.05), labels=cbind(16,29,10,23), cex=0.65)
text(cbind(-0.05,-0.05,-0.05), cbind(-0.3333333,-0.6666667,-1), labels=cbind(29,10,23), cex=0.65)
text(cbind(-0.05,-0.05,-0.05,-0.05,-0.05,-0.05,-0.05),cbind(0.06060606,0.2121212,0.3636364,0.5151515,0.6666667,0.8181818,0.969697), labels=cbind(50,100,150,200,250,300,350), cex=0.65)
text(cbind(-0.1666667,-0.3333333,-0.5,-0.6666667, -0.8333333, -1), cbind(-0.05,-0.05,-0.05,-0.05,-0.05,-0.05), labels=cbind(3.5,4,4.5,5,5.5,6), cex=0.65)

midpoint=(max(FlW_sc)+QtW_sc)/2
text(0.6666667, midpoint, labels = "FEV",cex=0.8125)


# Where expression is used: [14],[15] <- latter: How to correctly insert non-ASCII characters
mtext(expression("Discharge [m"^"3"~"/s]"), 3)
text(1.1, QtW_sc, expression("Q"[t])) 
text(0.6666667, -0.25, expression("T"[f]), cex=0.75)
text(-htW_sc, -1.1, expression("h"[t]))

text(0.5, -0.45, expression("FEV" %~~%  "28.00 Mm" ^ "3"),cex=1)
text(0.37, -0.6, expression("h"[t]), cex=1) 
text(0.5, -0.6,labels = "= 4.8 m", cex=1)
text(0.35, -0.75, expression("Q"[t]), cex=1)
text(0.545, -0.75, expression("= 300 m" ^ "3"~"/s"), cex=1) 
# 300 given by [25]
text(0.33, -0.9, expression("T"[f]), cex=1) 
text(0.54, -0.9, labels = "= 229.75hrs", cex=1) 

segments(0.2083332, -0.35, ScVecDW[lSVD], -0.35, lty=1, lwd=2) 
segments(0.2083332, -1, ScVecDW[lSVD], -1, lty=1, lwd=2)
segments(0.2083332, -0.35, 0.2083332, -1, lty=1, lwd=2)
segments(ScVecDW[lSVD], -0.35, ScVecDW[lSVD], -1, lty=1, lwd=2)

