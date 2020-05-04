#7->6->3->2->1
t=int(input())
n=[]
for i in range(t):
    n+=[input()]
n1 = [int(x) for x in n]
for n in n1:
    count=0
    while n != 1:
        #print(n,count)
        if n%2==0:
            n = int(n/2)
            count+=1
        else:
            n -=1
            count+=1
        if n == 1:
            break    
    print(count)