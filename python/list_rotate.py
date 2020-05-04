l=[34,23,12]
#rotate right clockwise
print(l)
out=[]
out.append(l[-1])
for i in range(0,len(l)-1):
    out.append(l[i])
print(out)


#rotate left anticlockwise

out=[]
for i in range(1,len(l)):
    out.append(l[i])
out.append(l[0])
print(out)

def rotate(l):
    l=[l[-1]]+l
    l.pop()
    return l

print(rotate([1,2,3,4,5
]))