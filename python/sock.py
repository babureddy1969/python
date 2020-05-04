def sockMerchant(n, ar):
    count=0
    for item in set(ar):
        #print(ar.count(item))
        if ar.count(item) %2 == 0:
            count+=ar.count(item)/2
        else:
            count += (ar.count(item)-ar.count(item)%2)/2
    return int(count) 
n=9
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]    
print(sockMerchant(n,ar))