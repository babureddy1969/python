# for i in range(10): # i can take values from 0 - 10
#     print(i)
# for i in range(20):
#     print(i)
# for i in range(1,10, 2):#1,3,5,7,9
#     print(i)
# for i in range(10,  0,  -1): #10-1 
#     print(i)
# for i in range(10,  0,  -3): #10-1 
#     print(i)
# s = 'hello'
# for character in s: #s becomes array of characters
#     print(character)
# for index in range(len(s)):
#     print(s[index])
s = "This is a long string"
# if len(s) > 10:
#     for index in range(10):
#         print(s[index], end='')

# for ch in s:
#     if ch == 'a':
#         print ('found a')
#     elif ch == 'e':
#         print ('found e')
#     elif ch == 'i':
#         print ('found i')
#     elif ch == 'o':
#         print ('found o')
#     elif ch == 'u':
#         print ('found u')

# print('There are {} a'.format(s.count('a')))
# print('There are {} e'.format(s.count('e')))
# print('There are {} i'.format(s.count('i')))
# print('There are {} o'.format(s.count('o')))
# print('There are {} u'.format(s.count('u')))

s = 'ABCDE1234G'
# for ch in s:
#     if ch.isdigit():
#         print(ch,end='')

# convert time from  12 hour format to 24 hour format
# to 12:30 AM 0030 HOURS 
# 01:30 PM == 1330 HOURS
# 10:30 PM == 2230 HOURS
# 12:30 AM == 1230 HOURS
# 00:10 AM == 0010 HOURS
t = "12:30 AM" # 0030 HOURS

# print ('-' * 10)
# print ('_' * 10)
'''
*
**
***
****
*****
'''
# for i in range(1,5):
#     print('*' * i)
# print ('{:^5}'.format('*'))
# print ('{:^6}'.format('* *'))
# print ('{:^6}'.format('* * *'))
# print ('{:^6}'.format('* *'))
# print ('{:^5}'.format('*'))

print ('{:<5}'.format('*')) # star will appear to left
print ('{:>5}'.format('*'))# star will appear to right

