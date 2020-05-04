#sorting a millon entries.
import random,datetime
x=0
list1=[random.randint(1,10000) for x in range(10000)]
t1=datetime.datetime.now()
for i in list1:
    if i == 10:
        print('found',i)
        break
t2=datetime.datetime.now()
print(t2-t1)
