String1 = 'I\'m a "Geek"'
print(String1) 

#palindrome
s="lesson"
p=True
for i in range(1,int(len(s)/2)):
    if s[i] != s[-1 * (i+1)]:
        print(s , "is not a palindrome")
        p=False
        break
if p:
    print(s, "is a palindrome")

#reverse a string
s="lesson"
s1=""
for i in range(0,len(s)):
    s1 += s[-1 * (i+1)] 
print(s1)

#reverse a string
s="lesson"
s1=""
for i in range(len(s)-1,-1,-1):
    s1 += s[i] 
print(s1)


#anagrams

#string formatting

# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print(String1) 

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print(String1) 

# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print(String1) 

# Python Program for 
# Old Style Formatting 
# of Integers 

Integer1 = 12.3456789
print('The value of Integer1 is %3.2f' %Integer1) 
print('The value of Integer1 is %3.4f' %Integer1) 

#string chars in a string
s1="madam"
s2="dam"
if s2 in s1:
    print (s2, " in ",s1)
else:
    print(s2, " not in ", s1)
    found=True
    for a in s2:
        if a not in s1:
            print("chars in ", s2, " not in ", s1)
            found = False
            break
    if found:
        print("chars of",s2,' in ', s1)

#max(s1) #m
#min(s1) #a
def indianFormat(s1):
    #format amount
    #s1 = "102030"
    s2=''
    if len(s1)>3:
        s1 = s1[:-3]+','+s1[-3:]
    #print (s1)
    for i in range (len(s1)-3,2):
        s2+=s1[i:i+2]+','
    #print(s2)

def sayHello():
    print("Hello!")
#h=sayHello
#h()
def indianFormat(n):
    if not n.isdigit():
        print(n,"is not a number")
        return n
    if len(n)<3:
        return n
    f=','+n[-3:]
    num=n[:-3]
    skip=2
    for s in range(len(num)-1,-1,-1):
        f = num[s]+f
        skip -= 1
        if skip == 0 and s>0:
            f = ',' + f
            skip=2
    #print(f)
    return f

#indianFormat("1000000")
s="10000"
def formatUS(s):
    s1=''
    skip=3
    for i  in range(len(s)-1,-1,-1):
        if skip == 0:
            s1 =','+s1
            skip=3
        s1=s[i] + s1
        skip -= 1

    return s1
#print(formatUS("10000000"))

s=''' This is python class. Tomorrow
    is java class. I am a working professional'''

#print (s)    
'''for s in s.split('\n'):
    print(s)
for s in s.split('.'):
    print(s)
'''
def rotateRight(s,n):
    s1='abcdefghijklmnopqrstuvwxyz'
    s11='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s2=s1
    s22=s11
    s3=''
    for i in range(n):
        s2=s2[1:len(s2)]+s2[0]
    for i in range(n):
        s22=s22[1:len(s22)]+s22[0]
    for a in s:
        if a in s1: 
            s3 += s2[s1.index(a)]
        elif a in s11: 
            s3 += s22[s11.index(a)]
        else:
            s3+=a
    return s3
#print(rotateRight('There\'s-a-starman-waiting-in-the-sky',2))
print(rotateRight('middle-Outz',2))