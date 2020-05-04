import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
print(x,type(x))
x = json.loads(x)
print(x,type(x))
x = json.dumps(x)
print(x,type(x))
