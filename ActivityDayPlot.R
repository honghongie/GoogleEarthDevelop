setwd("E:/R_project")
library(plotKML)
library(sp)
timeslot<-read.table("TowerActivityDay.txt",header=FALSE,sep=",")
colnames(timeslot)<-c("towerid","weekday","weekend")
View(timeslot)
geo<-read.csv("TowerGeo.csv",header=FALSE)
nrow(geo)
View(geo)
nrow(timeslot)

for (i in 1:nrow(timeslot))
{
  for (j in 1:nrow(geo))
  {
    if(geo[j,1]==timeslot[i,1])
    {
      timeslot[i,4]=geo[j,2]
      timeslot[i,5]=geo[j,3]
    }
  }
}

View(timeslot)
write.csv(timeslot,"TowerActDayGeo.csv")

data<-timeslot[complete.cases(timeslot),]
View(data)


colnames(data)<-c("id","weekday","weekend","lon","lat")
View(data)

sp <- SpatialPoints(data[,c("lon","lat")])
proj4string(sp) <- CRS("+proj=longlat +datum=WGS84")

df1<-data.frame(data$weekday)
View(df1)
xy.spdf<-SpatialPointsDataFrame(sp,df1)
View(xy.spdf)
bubble(xy.spdf["data.weekday"])
plotKML(xy.spdf["data.weekday"])

df2<-data.frame(data$weekend)
xy.spdf<-SpatialPointsDataFrame(sp,df2)
View(xy.spdf)
bubble(xy.spdf["data.weekend"])
plotKML(xy.spdf["data.weekend"])



