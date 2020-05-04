'''d = input('Please enter date 1, date 2 in the format yyyy mm dd: ').split()

y1,m1,d1,y2,m2,d2=int(d[0]),int(d[1]),int(d[2]),int(d[3]),int(d[4]),int(d[5])

d = abs(d1-d2)
m = abs(m1-m2)
y = abs(y1-y2)

print (y1,m1,d1)
print (y2,m2,d2)
print (y,m,d)
'''
from datetime import date

d0 = date(2018, 10, 11)
d1 = date(2019, 12, 1)
delta = d1 - d0
#print(delta.days)

'''
5 4 4 2 2 8     
3 2 2 0 0 6      ==> 6
1 0 0 0 0 4      ==> 4
1 0 0 0 0 2      ==> 1
1 0 0 0 0 1      ==> 1
'''
arr=[5, 4, 4, 2, 2, 8]
arr=[1, 2, 3, 4, 3, 3, 2, 1]
m = min(arr)
#print(m)
result=[]
while True:
    done=True
    count=0
    for i in range(len(arr)):
        #print(arr[i],m)
        if arr[i] >= m:
            arr[i] -= m
            count+=1
        elif arr[i] < m and arr[i]>0:
            arr[i] = 0
            count+=1
        if arr[i]>=m: done=False
    result+=[count]
    print(arr,count)
    if done:
        break
#print (result)
#sreturn result    


m=min(arr)
while(len(arr)>0):
    count=0
    for i in range(len(arr)):
        if arr[i]>=m: 
            arr[i]-=m
            count+=1
        elif arr[i]>0 and arr[i] < m:    
            arr[i]=0
            count+=1
    result+=[count]
    for i in range(arr.count(0)):        
        arr.remove(0)
print(result)