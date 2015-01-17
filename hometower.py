import os,sys
rpath="/home/lingzi/cdr/CleanCDR3Result2/TowerActivityNew/"
wpath="/home/lingzi/cdr/CleanCDR3Result2/"
dictphone={}
fw=open(wpath+"phonehome.txt",'w')

for item in os.listdir(rpath):
	f=open(rpath+item)
	tower=item[:-4]
	for line in f:
		strs=line.split(",")
		if len(strs)==4:
			time=strs[1]
			hour=int(time[0:2])
			
#calculate record later than 6:00pm
			if hour>17:
				phone=strs[2]
				
				if dictphone.has_key(phone):
					alist=dictphone[phone]
					alist.append(tower)
					dictphone[phone]=alist
				else:
					dictphone[phone]=[tower]
#calculate most common tower in the phone after 6:00pm
def most_common(lst):
	return max(set(lst), key=lst.count)

for key in dictphone:
	alist=dictphone[key]
	hometower=most_common(alist)
	fw.write(key+","+hometower+"\n")
fw.close()

#calculate how many phone have a home tower
phonehashome=len(dictphone)
print(phonehashome)


