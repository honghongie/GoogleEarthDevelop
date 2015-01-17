import os,sys
path="/home/lingzi/cdr/CleanCDR3Result2/"
dicttowerlong={}
dicttowerlat={}
dictphonecentre={}

fgeo=open(path+"UniqueTowers.txt")
#fUnique=open(path+"phoneuniquetowers.txt")
ftowers=open(path+"phonetowers.txt")
fw=open(path+"PhoneCenter.txt",'w')

for line in fgeo:
	strs=line.split(",")
	tower=strs[0]
	longitude=float(strs[1])
	latitude=float(strs[2])
	print(longitude)
	print(latitude)
	dicttowerlong[tower]=longitude
	dicttowerlat[tower]=latitude

for line in ftowers:
	words=line.split(",")
	phone=words[0]
	longi=0
	lati=0
	for i in range(len(words)-1):
		tid=words[i+1].strip()
		longi=longi+dicttowerlong[tid]
		lati=lati+dicttowerlat[tid]
	cenlongi=longi/(len(words)-1)
	cenlati=lati/(len(words)-1)
	cenpoint=str(cenlongi)+","+str(cenlati)
	dictphonecentre[phone]=cenpoint

for key in dictphonecentre:
	fw.write(key+","+dictphonecentre[key]+"\n")

