l=[1,2,3,4]
for i in range(int(len(l)/2)):
    l[i] , l[-1*(i+1)] = l[-1*(i+1)],l[i]
print(l)

