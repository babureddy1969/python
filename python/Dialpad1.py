s='4938532894754'
s='5198155156'
#s='1234567'
if len(s) < 7:
    print('invalid',s)
    exit(0)
elif len(s) == 7 and len(set([s[i:i+1] for i in range(0, len(s), 1)])) ==7:
    for x in s : print(x,end=' ')      
    exit(0)
start=0
end=2
slices=[]
result=[]
while end <= len(s):
    slice = s[start:end]
    if result==[]:
        result+=[slice]
        start+=2
        end=start+2
    if slice in result:
        start+=1
        end=start+2    
        continue  
    else :
        if int(slice)+10 not in [int(x) for x in result]:
            result+=[slice[0]]
            start+=1
            end = start+2
        else:
            result+=slice
            start+=2
            end = start+2
for x in result : print(x,end=' ')        