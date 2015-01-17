#Connect index from  municipios to polygon
------------------------------------------------------------------------------
#MunicipiosIndex
#MunicipiosPolygonTowerCopy
MI<-read.csv("MunicipiosIndex.csv",header=TRUE,stringsAsFactors=FALSE)
str(MI)
View(MI)
MPT<-read.csv("MunicipiosPolygonTowerCopy.csv",header=TRUE,stringsAsFactors=FALSE)
str(MPT)
View(MPT)
nrow(MPT)
MPT<-MPT[complete.cases(MPT),]
for (i in 1:nrow(MPT))
{
  for (j in 1:nrow(MI))
  {
    if (MPT$COD_MUPIO[i]==MI$CODIGO_MUNICIPIO[j])
    {
      MPT[i,6]=MI[j,3]
      MPT[i,7]=MI[j,4]
      MPT[i,8]=MI[j,5]
      MPT[i,9]=MI[j,6]
      MPT[i,10]=MI[j,7]
    }
  }
}
View(MPT)

write.csv(MPT,"MuniPolyIndexAll.csv")
ratiosum<-aggregate(MPT$PERCENTAGE,by=list(MPT$Name),FUN=sum)
str(ratiosum)
nrow(ratiosum)
subratiosum<-ratiosum[which(ratiosum$x>95),]
nrow(subratiosum)
-------------------------------------------------------------------------------------
MPIA<-read.csv("MuniPolyIndexAll.csv",header=TRUE,stringsAsFactors=FALSE)
str(MPIA)
#subMPIA<-subset(MPIA,MPIA$COD_MUPIO>=700 & MPIA$COD_MUPIO<1000)
#not able to include points in the city but polygon overlap to other cities.
towermuni<-read.csv("Municipios3Tower.csv",header=TRUE)
View(towermuni)
towerlist<-towermuni[,6]
length(towerlist)
towerlist<-unique(towerlist)
subMPIA<-MPIA[MPIA$towerid %in% towerlist,]
nrow(subMPIA)
subMPIA$towerid<-as.factor(subMPIA$towerid)
levels(subMPIA$towerid)
View(subMPIA)
write.csv(subMPIA,"threeCitiesMPI.csv")
---------------------------------------------------------------------------------
#aggregate to see whether sum of polygon percentage is 100%
subMPIA$Name<-as.factor(subMPIA$Name)
ratiosum<-aggregate(subMPIA[,12],by=list(subMPIA$Name),FUN=sum)
ratiosum
nrow(ratiosum)
subratiosum<-ratiosum[which(ratiosum$x>0.9),]
nrow(subratiosum)
------------------------------------------------------------------------------------
#aggregation of index: calculate percentage of each part
nrow(subMPIA)
head(subMPIA[,5])
length(towerlist)
nrow(subMPIA)
for (j in 1:nrow(subMPIA))
{
  subMPIA[j,12]<-subMPIA$PERCENTAGE[j]/(sum(subMPIA[which(subMPIA$towerid==subMPIA$towerid[j]),5]))
}
View(subMPIA)

for (i in 1:nrow(subMPIA))
{
  subMPIA[i,7:11]<-subMPIA[i,7:11]*subMPIA[i,12]
}

Incidencia<-aggregate(subMPIA[,7],by=list(subMPIA$towerid),FUN=sum)
Brecha<-aggregate(subMPIA[,8],by=list(subMPIA$towerid),FUN=sum)
Severidad<-aggregate(subMPIA[,9],by=list(subMPIA$towerid),FUN=sum)
Incidencia.1<-aggregate(subMPIA[,10],by=list(subMPIA$towerid),FUN=sum)
Gini<-aggregate(subMPIA[,11],by=list(subMPIA$towerid),FUN=sum)

TowerIndex<-data.frame(Incidencia,Brecha,Severidad,Incidencia.1,Gini)
View(TowerIndex)
str(TowerIndex)
threeCityTowerIndex<-data.frame(TowerIndex$Group.1,TowerIndex$x,TowerIndex$x.1,TowerIndex$x.2,
                                TowerIndex$x.3,TowerIndex$x.4)
write.csv(threeCityTowerIndex,"threeCityTowerIndex.csv")
