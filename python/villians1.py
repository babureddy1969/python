

v=[10, 20, 50, 100, 500, 400] 
e=[30, 20, 60, 70, 90, 490] 

v=[10, 20, 30, 40, 50] 
e=[40, 50, 60, 70, 80]

'''5
10 20 30 40 50 
40 50 60 70 80'''
cases=input()
for i in range(int(cases)):
    count = int(input())
    v = input().split()
    e = input().split()
	if len(v)>len(e):
		print('LOSE')
		continue
    e = [int(numeric_string) for numeric_string in e]
    v = [int(numeric_string) for numeric_string in v]
	
	v.sort()
	e.sort()
	lost=False
	for i in range(len(v)):
		if v[i]>e[i]:
			print('LOSE')
			lost=True
			break
	if not lost:
		print('WIN')