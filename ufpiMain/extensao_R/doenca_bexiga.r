install.packages('survival')
install.packages('flexsurv')

require(flexsurv)
require(flexsurv)

tempos <- c(3,5,6,7,8,9,10,10,12,15,18,19,20,22,25)
cen <- c(1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0)

ekm <- survfit(Surv(tempos, cen)~1)
summary(ekm)