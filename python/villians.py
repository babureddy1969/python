

v=[10, 20, 50, 100, 500, 400] 
e=[30, 20, 60, 70, 90, 490] 

v=[10, 20, 30, 40, 50] 
e=[40, 50, 60, 70, 80]

'''5
10 20 30 40 50 
40 50 60 70 80'''
cases=input('how many cases')
for i in range(int(cases)):
    count = int(input("How many villians?"))
    v = input('Enter villian powers').split()
    v = [int(numeric_string) for numeric_string in v]
    e = input('Enter hero powers').split()
    e = [int(numeric_string) for numeric_string in e]
    if max(e) < max(v):
        print('LOSE')
    else:
        while len(e)>0 and max(e)>max(v):
            if max(e)>=max(v):
                v.remove(max(v))
                e.remove(max(e))
            else:
                print('LOSE')
                break
    if len(v)==0:
        print('WIN')