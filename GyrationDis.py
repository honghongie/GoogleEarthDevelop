import os,sys
import math
path="/home/lingzi/cdr/CleanCDR3Result2/"

#PhoneCenter.txt
#phoneuniquetowers.txt
#UniqueTowers.txt

dicttowerlong={}
dicttowerlat={}
dictcenlong={}
dictcenlat={}
dictphonedis={}

fgeo=open(path+"UniqueTowers.txt")
fUnique=open(path+"phoneuniquetowers.txt")
fcenter=open(path+"PhoneCenter.txt")
fw=open(path+"GyrationDis.txt",'w')

#define dist calculation function
def distance(long1,lat1,long2,lat2):
	R=6371
	degtoradi=0.0174532925
	
	long1=long1*degtoradi
	lat1=lat1*degtoradi
	long2=long2*degtoradi
	lat2=lat2*degtoradi

	la=lat2-lat1
	lo=long2-long1
	a=math.sin(la/2)*math.sin(la/2)+math.cos(lat1)*math.cos(lat2)*math.sin(lo/2)*math.sin(lo/2)
	c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
	dist=R*c
	return dist

for line in fgeo:
	strs=line.split(",")
	tower=strs[0]
	longitude=float(strs[1])
	latitude=float(strs[2])
	dicttowerlong[tower]=longitude
	dicttowerlat[tower]=latitude

for line in fcenter:
	words=line.split(",")
	pid=words[0]
	dictcenlong[pid]=float(words[1])
	dictcenlat[pid]=float(words[2])

for line in fUnique:
	strings=line.split(",")
	phoneid=strings[0]
	gyrationdist=0
	centerlong=dictcenlong[phoneid]
	centerlat=dictcenlat[phoneid]
	if len(strings)==2:
		dictphonedis[phoneid]=0
	else:
		for i in range(len(strings)-1):
			tid=strings[i+1].strip()
			tlong=dicttowerlong[tid]	
			tlat=dicttowerlat[tid]
			gyrationdist=gyrationdist+distance(centerlong,centerlat,tlong,tlat)
		dictphonedis[phoneid]=gyrationdist

for key in dictphonedis:
	fw.write(key+",%f\n"% dictphonedis[key])
fw.close()

