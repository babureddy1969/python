l=[0, 0, 1, 0, 0, 1, 0]
jump=0
index=0
current=l[0]
for i,v in enumerate(l):
    if i<len(l)-1 :
        #print(v,l[i+1])
        if v == 0 and l[i+1] == 0:
            if i<len(l)-2 and v==0 and l[i+2] == 0:
                jump+=1
                
        elif i<len(l)-2 and v==0 and l[i+2] == 0:
            jump+=1
    
    
print (jump)