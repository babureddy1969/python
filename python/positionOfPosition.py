def permutationEquation(p):
    l=[]
    for x in range (1,len(p)+1):
        l+=[p[p.index(x)]]
    return l
p=[2,3,1]
#print(permutationEquation([2,3,1]))
#print(permutationEquation([5,2,1,3,4]))

def x(p):
    
    q = []
    for i in p:
        q+=[p[p[i-1]-1]-1] 
    
    return q
print(x([2,3,1]))