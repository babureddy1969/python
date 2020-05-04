import math

def getNext(x):
    for i in range(x,0,-1):
        if math.sqrt(i) % 2 == 0.0:
            return i

winner = 'Louise'
n=6

while True:
    if n==1:
        return winner
    if math.sqrt(n) == 0.0:
        winner='Richard'
    else:
        i=n-getNext(n)
        winner='Richard'
    
    if i%2 == 0.0:


print(winner)