n = int(input())
for _ in range(n):
    s=input()
    if len(s) < 7:
        #print('invalid',s)
        exit(0)
    elif len(s) == 7 and len(set([s[i:i+1] for i in range(0, len(s), 1)])) ==7:
        print(s,'->',end='')
        for x in s : print(x,end=' ')      
        print()
        exit(0)
    start=0
    end=2
    slices=[]
    result=[]
    while end <= len(s):
        slice = s[start:end]
        if slice[0] != slice[1]:
            if slice not in result :
                if slice[1]+slice[0] not in result:
                    result+=[slice]
                    start+=2
                    end=start+2      
                elif int(slice)+10 not in [int(x) for x in result]:
                    result+=[slice[0]]
                    start+=1
                    end = start+2
                else:
                    result+=[slice[0]]
                    start+=1
                    end = start+2
        else:
            if slice[0] not in result:
                result+=[slice]
            start+=1
            end=start+2
    print(s,'->',end='')
    for x in s : print(x,end=' ')      
    print()

