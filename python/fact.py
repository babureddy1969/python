factor=1
n=100
while factor <= n:
	#print('factor =', factor, ' n =', n)
	if n % factor == 0:
		print(factor, end=' ')
	factor += 1 #
	
number = 100	
for i in range (1,number+1):
	if number % i == 0:
		print (i)