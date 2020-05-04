#even to odd

l=[1,2,3,4,5]
def isEven(n):
    return n%2 == 0
def isOdd(n):
    if n%2==0:
        return False
    for i in range (3,n,2):
        if n%i==0:
            return True
    return False
def evenToOdd(n):
    while True:
        n=n+1
        if isEven(n):
            continue
        if isOdd(n):
            return n

for i in l:
    if isEven(i):
        l[l.index(i)]=evenToOdd(i)
print(l)