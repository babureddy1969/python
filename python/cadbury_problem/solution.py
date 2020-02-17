def TotalCount(M,N,P,Q):
    count=0
    for l in range(M,N+1):
        for b in range(P,Q+1):
            count +=CountPerChocolateBar(l,b)
    return count

def CountPerChocolateBar(l,b):

  count = 0
  while True:
      longer=max(l,b)
      shorter=min(l,b)
      count+=1
      diff=longer-shorter
      if diff==0:
        return count
      else :
        l=min(l,b)
        b=diff   

M=int(input("Number: "))

N=int(input("Number: "))
P=int(input("Number: "))
Q=int(input("Number: "))
tc=TotalCount(M,N,P,Q)

print (tc)