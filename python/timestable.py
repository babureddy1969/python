print ("      1  2  3  4  5  6  7  8  9  10")
print ("-----------------------------------")
for row in range (1,11):
	r = str(row)
	if row<10:  
		r +="  |  "
	else: 
		r += " |  "
	for col in range (1,11):
		val = row*col
		r += str(val) 
		if val<10:
			r += "  "
		else:
			r += " "
	print (r,"\n")
