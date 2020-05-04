#functions examples

#simple interest
def simpleInterest(P,T,R):
    SI = P * T * R / 100
    A = SI + P
    return SI, A
# while True:    
#     P=input("Enter principle:")
#     T=input("Enter time:")
#     R=input("Enter rate:")
#     SI,A = simpleInterest(float(P), float(T), float(R))
#     print (P,T,R,SI,A)
#     choice=input("Enter q to quit:")
#     if choice == 'q': break

def reverseString(item):
    output=""
    for i in range(len(item)-1,-1,-1):
        output+=item[i]
    return output
s='hello'
#print(s,reverseString(s))
#0 1 1 2 3 5 8 13 21 34
def fib(n=10):
    a=0
    b=1
    output=[a,b]
    for _ in range(n):
        c=a+b
        a=b
        b=c 
        output+=[c]
    return output
# print(fib(10))
# print(fib(5))
# print(fib(8))


#s1=listen
#s2=silent
def areTheseAnagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c not in s2:
            return False
    return True
s1='listen'
s2='silent'
result = areTheseAnagrams(s1,s2)
print(s1,s2,result)
s1='hello'
s2='hi'
result = areTheseAnagrams(s1,s2)
print(s1,s2,result)
