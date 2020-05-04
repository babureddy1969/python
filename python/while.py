#for i in range(1,11):
#    print(i)
i=1
while i <11:
#    print(i)
    i = i +1
# i=0 # initializa i to 0
# while True: # define while loop - infinite
#     print(i,end=' ') # statement executed inside while loop
#     if i<0: # condition
#         break # exit the loop
#     i += 1 # increment i by 1

# name = input('Enter your name :')
# age = input('Enter your age :')
# print(name,age)
# total = 0
# count = 0
# while True :
#     value = input('Enter a number: ')
#     if value == 'done' : break
#     value = float(value)
#     total = total + value
#     count = count + 1
#     average = total / count
# print ('Average:', average)

# numlist = list()
# while True :
#     value = input('Enter a number: ')
#     if value == 'done' : break
#     value = float(value)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print ('Average:', average)

while True:
    num = input("Enter a number :")
    if int(num) % 2 == 0: continue
    else: break    
while True:
    num = input("Enter a number :")
    if int(num) % 2 != 0: break
