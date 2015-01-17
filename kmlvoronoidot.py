import os,sys
path="E:/"
f2=open(path+"RMduplicateTower.txt")
f=open(path+"output.txt")
wf=open(path+"TowerActivity.kml",'w')

wf.write('<?xml version="1.0" encoding="UTF-8"?>\n')
wf.write('<kml xmlns="http://earth.google.com/kml/2.0"> <Document>\n')

wf.write('<Style id="My_Style">\n')
wf.write('<IconStyle> <scale>1</scale><Icon>\n')
wf.write('<href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href>\n')
wf.write('</Icon></IconStyle>\n')
wf.write('<BalloonStyle> <text>$[description]</text> </BalloonStyle>\n')
wf.write('</Style>\n')

strs=f.readlines()
i=0
j=0
while i < len(strs):
	if len(strs[i].split())==3:
		j=j+1
		wf.write("<Placemark>\n")
		wf.write("<name>\n")
		wf.write("Area#%d</name>\n"% j)
		wf.write("<description>\n")
		wf.write("</description>\n")
		wf.write("<Polygon><outerBoundaryIs>  <LinearRing>\n")
		wf.write("<coordinates>\n")
		while strs[i].strip():
			a=strs[i].split()
			xlong=a[1]
			ylat=a[2]
			wf.write(xlong+","+ylat+",0.0\n")
			i=i+1
			if i==len(strs): break
		wf.write("</coordinates>\n")
		wf.write("</LinearRing> </outerBoundaryIs> </Polygon>\n")
		wf.write("<Style>\n")
		wf.write("<LineStyle><color>ff000000</color></LineStyle>")
		
		wf.write("<PolyStyle>\n")
		wf.write("<color>00ffffff</color>\n")
		wf.write("<fill>1</fill>\n")
		wf.write("<outline>1</outline>\n")
		wf.write("</PolyStyle>\n")
		wf.write("</Style>\n")
		wf.write("</Placemark>\n")
	else:
		i=i+1

for line in f2:
	strs2=line.split(",")
	if len(strs2)==3:
		towerid=strs2[0]
		longitude=strs2[1]
		latitude=strs2[2]
		wf.write("<Placemark>\n")
		wf.write('<description><![CDATA[\n')
		wf.write('<font size=6>'+towerid+'</font><br>\n')
		wf.write('<center>\n')
		wf.write('<img src="./TowerPlot/'+towerid+'.png" width="350" hight="350">\n')
		wf.write('</center>]]></description>\n')
		wf.write("<styleUrl> #My_Style</styleUrl>\n")
		wf.write("<Point><coordinates>\n")
		wf.write(strs2[1]+","+strs2[2])
		wf.write(" </coordinates></Point>\n")
		wf.write("</Placemark>\n")

wf.write("</Document></kml>")
wf.close()





		
		

			
			

	
