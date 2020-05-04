import time

sum = 0
i=0
start = time.time()
while i < 10000000:
    sum = sum + i
    #print (i,sum)
    i = i + 1
print (i,sum)
print (time.time()-start)
import test
'''if (i>1000):
    import test1 as test
else:
    import test2 as test'''
print (test.show())