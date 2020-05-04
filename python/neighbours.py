'''5
5
-1 7 8 -5 4 
4
3 2 1 -1 
4
11 12 -2 -1 
4
4 5 4 3 
4
5 10 4 -1'''
def main():	
    t = int(input())	
    while(t>0):	
        t-=1	
        n = input()
        arr = [int(x) for x in input().split()]	
        arrod = []	
        arrev = []	
        for i in range(0,n,2): 
            arrod.append(arr[i])	
            for j in range(1,n,2):	
                arrev.append(arr[j])	
                arrmax = max(arr)	
                d = {}	
                for k in range(1,len(arrod)):	
                    if (arrod[k-1]+arrod[k]) >= arrmax:	
                        if (arrod[k-1]+arrod[k]) in d.keys():	
                            if d[arrod[k-1]+arrod[k]] < int(''.join(sorted([str(arrod[k]),str(arrod[k-1])]))) :	
                                d[arrod[k-1]+arrod[k]] = int(''.join(sorted([str(arrod[k]),str(arrod[k-1])])))	
                            else:	
                                d[arrod[k-1]+arrod[k]] = int(''.join(sorted([str(arrod[k]),str(arrod[k-1])]))) 
                                for m in range(1,len(arrev)):	
                                        if (arrev[m-1] + arrev[m]) >= arrmax:	
                                            if (arrev[m-1] + arrev[m]) in d.keys():	
                                                if d[arrev[m-1] + arrev[m]] < int(''.join(sorted([str(arrev[m])+str(arrev[m-1])]))):	
                                                    d[arrev[m-1] + arrev[m]] = int(''.join(sorted([str(arrev[m])+str(arrev[m-1])])))	
                                                else: 
                                                    d[arrev[m-1] + arrev[m]] = int(''.join(sorted([str(arrev[m])+str(arrev[m-1])])))	
                if len(d) == 0 :	
                    print(arrmax)	
                else:	
                    print(d[max(d.keys())])
main()