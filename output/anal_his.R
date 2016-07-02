require(boot)

raw = read.csv("COMBINED_corr_output.txt", header=F)
#raw = raw[raw$V1>0,]
wvec = raw[,-1]
plot( cor(raw)[1,-1], pch=16 )

f <- lm( V1 ~ V2+V3+V4+V5+V6, data=raw )
summary(f)

p <- prcomp(wvec)
s <- cumsum(p$sdev) / sum(p$sdev)
# take 52 pcs, 80%
plot(s, pch=16, cex=0.7)

pcs <- p$x[,1:105]
plot( cor( cbind(raw[,1], p$x) )[1,-1], pch=16 )

da <- data.frame("price"=raw[,1], pcs)
fit <- lm(price ~ . - price, data=da[-1,])
summary(fit)
plot(fit)

o = rep(0, nrow(da))
for( i in 1:nrow(da) ) {
  f <- lm(price ~ . - price, data=da[-i,])
  o[i] <- da[i,1] - predict(f, da[i,])
}
