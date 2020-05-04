for num in range(100,3,-1):
    isprime=True
    for i in range(2,num-1):
        if num%i == 0:
            isprime=False
            break
    if isprime:
        print(num)
        break