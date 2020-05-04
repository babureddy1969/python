val=input("Enter any value")
datatype=str(type(val))
if datatype.isnumeric():
    print("You entered a integer")
elif datatype.isalnum():
    print("You entered a string")
elif datatype.isdecimal():
    print("You entered a float")