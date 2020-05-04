import sys
def test():
    a = input ('number 1 ')
    b = input ('number 2 ')
    # if not a.isdigit():
    #     print("Please enter a number1")
    # if not b.isdigit():
    #     print("Please enter a number2")
    try:
        a = int(a)
        print(v1)
    except ValueError as v:
        print(sys.exc_info(),"Enter number for a")    
        exit(0)
    try:
        b = int(b)
    except:
        print("Enter number for b")
        exit(0)
    try:
        c = a/b
        print(a,b,c)
    except:
        print("B must be > 0")  
        b = '1'
        try:
            c = a/b  
        except:
            print("error while dividing by str")
test()
v1=0
