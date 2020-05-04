#odd numbers
s  = "odd numbers"
for i in range (3,100):
	for x in range(3,i-1):
		if i!=x and i%x == 0 and i%2 >0:
			s += str(i) + " "
			break
print(s)
