setwd("/Users/w4a2y4/Desktop/robohon-data")
blks <- read.csv("result/blocks.csv")
rt.aov <- aov(RT ~ eoc, blks) 
om.aov <- aov(omission ~ eoc, blks)
rtcv.aov <- aov(RTCV ~ eoc, blks)
anti.aov <- aov(anticipation ~ eoc, blks)
pb2.aov <- aov(probe2 ~ eoc, subset(blks, probe2 != -1))

summary(rt.aov) # ***
pairwise.t.test(blks$RT, blks$eoc) # all significant

summary(om.aov) # -

summary(rtcv.aov) # ***
pairwise.t.test(blks$RTCV, blks$eoc) # 2&01 significant

summary(anti.aov) # ***
pairwise.t.test(blks$anticipation, blks$eoc) # 2&01 significant

summary(pb2.aov) #**
pairwise.t.test(blks$probe2, blks$eoc) # all significant


library(stats)
oneway.test(RT ~ eoc, blks)
# F = 43.072, num df = 2.00, denom df = 97.79, p-value = 3.844e-14
oneway.test(RTCV ~ eoc, blks)
# F = 11.669, num df = 2.000, denom df = 94.204, p-value = 2.968e-05
oneway.test(omission ~ eoc, blks)
# F = NaN, num df = 2, denom df = NaN, p-value = NA
oneway.test(anticipation ~ eoc, blks)
# F = NaN, num df = 2, denom df = NaN, p-value = NA
oneway.test(probe2 ~ eoc, subset(blks, probe2 != -1))
# F = 4.1791, num df = 2.000, denom df = 27.428, p-value = 0.02605

