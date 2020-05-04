arr=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
d={}
for item in arr:
    d[item] = d.get(item,0)+1
maxvalue=max(d.values())
d=sorted(d.items(),reverse=True)
m={}
for k,v in d:
    if v == maxvalue:
        m[v]=k
print( m[maxvalue])