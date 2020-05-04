s={
    "name":"Ram",
    "age":30,
    "address":
        {"street1":"65,4th Main Road",
        "street2":"Mathikere",
        "city":"Bangalore",
        "state":"Karnataka"}
}
#for key in s.keys()    :
#    print(key,s[key])

def printRecursive(s):
    for key in s.keys()    :
        if isinstance(s[key],dict):
            printRecursive(s[key])
        else:
            print(key,s[key])
printRecursive(s)

#update
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)
'''{1: 'one', 2: 'two'}
{1: 'one', 2: 'two', 3: 'three'}'''

d = {'x': 2}

d.update(y = 3, z = 0)
print(d)

d.clear()

#copy
original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: ', new)

#from key

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys) #{'a': None, 'e': None, 'i': None,'o':None,'u':None}
print(vowels)

d.get('a',0) #dislay default if no key is found
person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.items()) #dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
print(list(sales.items())) #[('apple', 2), ('orange', 3), ('grapes', 4)]

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

result = person.popitem() #('salary', 3500.0)
print('person = ',person)
print('Return Value = ',result)

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)


# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

l = [1, 3, 4, 0]
print('one false any result',any(l))

l = [0, False]
print('all false any output',any(l))

l = [0, False, 5]
print('one true any value',any(l))

l = []
print('empty any value',any(l))

# all values true
l = [1, 3, 4, 5]
print('all true values',all(l))

# all values false
l = [0, False]
print('all false values',all(l))

# one false value
l = [1, 3, 4, 0]
print('one false value',all(l))

# one true value
l = [0, False, 5]
print('one true value',all(l))

# empty iterable
l = []
print('empty iterable',all(l))

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))


testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using max(iterable, *iterables, key)
print('Maximum is:', max(num, num1, num2, key=len))

num = [15, 300, 2700, 821]
num1 = [12, 2]
num2 = [34, 567, 78]

# using min(iterable, *iterables, key)
print('Minimum is:', min(num, num1, num2, key=len))

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string 
pyString = 'Python'
print(sorted(pyString))

# set
pySet = {'e', 'a', 'u', 'o', 'i'}
print(sorted(pySet, reverse=True))

# dictionary
pyDict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(pyDict, reverse=True))

# frozen set
pyFSet = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(pyFSet, reverse=True))

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)

# start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)

numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting itertor to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)

# Converting itertor to set
resultSet = set(result)
print(resultSet)
