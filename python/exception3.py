a = input('Enter number a')
b = input ('Enter number b')
try:
    if not a.isdigit():
        raise ValueError("a is not a number!")
    if not b.isdigit():
        raise ValueError("b is not a number!")
    a = int(a)
    b = int (b)
    if b<=0:
        raise ZeroDivisionError("b has to be > 0")
    c = a/b
except ValueError as v:
    print(v )
except  ZeroDivisionError as z:
    print(z)