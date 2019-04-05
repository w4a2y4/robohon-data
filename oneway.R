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

