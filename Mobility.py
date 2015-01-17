import math
import os,sys
path="/home/lingzi/cdr/CleanCDR3Result2/"
fr=open(path+"phoneordertowers.txt")
fUnique=open(path+"UniqueTowers.txt")
fw=open(path+"Mobilityphone.txt",'w')
dictphone={}
dicttowerlong={}
dicttowerlat={}
#build tower geo dict
for lines in fUnique:
	words=lines.split(",")
	tid=words[0]
	dicttowerlong[tid]=float(words[1])
	dicttowerlat[tid]=float(words[2].strip())
print len(dicttowerlong)
print len(dicttowerlat)

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

for line in fr:
	strs=line.split(",")
	pid=strs[0]
	count=len(strs)-1
	mobdist=0
	if count==1:
		dictphone[pid]=0
	else:
		for i in range(1,count):
			tower1=strs[i]
			tower2=strs[i+1].strip()
			long1=dicttowerlong[tower1]
			lat1=dicttowerlat[tower1]
			long2=dicttowerlong[tower2]
			lat2=dicttowerlat[tower2]
			mobdist=mobdist+distance(long1,lat1,long2,lat2)
		dictphone[pid]=mobdist

for key in dictphone:
	fw.write(key+",%f\n"% dictphone[key])
fw.close()

			
					
