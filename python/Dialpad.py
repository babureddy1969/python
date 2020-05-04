import copy
s= "569815571556"
s='4938532894754'
result=[]
if len(s)>7:    
    n=2
    slices=[s[i:i+n] for i in range(0, len(s), n)]
    temp = copy.copy(slices)
    print(slices)
    result+=[slices[0]]
    for slice in slices[1:]:
        if slice not in result :
            if len(slice)==2 and slice[1]+slice[0] in result:
                subslices = [slice[0],slice[1]]
                if slice[0] not in result:
                    result+=[slice[0]]

            result += [slice]
            

if len(result) == 7:
    print(result)
else:
    print('invalid', result)
