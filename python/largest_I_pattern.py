arr = [
    [-9, -9, -9,  1, 1, 1], 
    [0, -9,  0,  4, 3, 2],
    [-9, -9, -9,  1, 2, 3],
    [0,  0,  8,  6, 6, 0],
    [0,  0,  0, -2, 0, 0],
    [0,  0,  1,  2, 4, 0]
]
arr=[
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0],
]
row=0
col=0
sum=0
for row in range(0,4):
    for col in range(0,4):
        t = arr[row][col]+arr[row][col+1]+arr[row][col+2]+ arr[row+1][col+1]+ arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
        sum = t if t > sum else sum
#         print (t)
#         print(arr[row][col],arr[row][col+1],arr[row][col+2], arr[row+1][col+1], arr[row+2][col],arr[row+2][col+1],arr[row+2][col+2])
print(sum)
# row=0
# col=1
# t = arr[row][col]+arr[row][col+1]+arr[row][col+2]+ arr[row+1][col+1]+ arr[row+2][col]+arr[row+2][col+1]+arr[row+2][col+2]
# sum = t if t > sum else sum
# print (t)
