i=2
s=i/2

while abs(s*s - i) > 0.000001:
    if s*s > i:
        s -= s/2
    else:
        s += s/2
print (s, s*s)
