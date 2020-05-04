arr=[0, 0, 0, 0, 1, 0]
prev=arr[0]
jump=0
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if arr[i] == arr[j] == 0:
            jump+=1
    
