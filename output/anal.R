raw = read.csv("COMBINED_-2_output.txt", header=F)
#raw = raw[raw$V1!=0, ]
wvec = raw[,-1]
#plot( cor(raw)[1,-1], pch=16 )

p <- prcomp(wvec)
s <- cumsum(p$sdev) / sum(p$sdev)
# take 58 pcs, 80%
plot(s, pch=16, cex=0.7, ylab="Cumulated Variation", xlab="PC Index")

pcs <- p$x[,1:58]
plot( cor( cbind(raw[,1], pcs) )[1,-1], pch=16, ylab="Correlation", xlab="PC Index" )

da <- data.frame("price"=raw[,1], pcs)
fit <- lm(price ~ . - price, data=da)
summary(fit)
