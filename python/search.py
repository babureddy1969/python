# my list 
test = ['Line', 'Text', 'Text', 'Line', 'Text', 'Line', 'Rectangle']
#output and input for splitting is 
input = ['Text', 'Line']
output = [['Line'], ['Text'], ['Text', 'Line'], ['Text', 'Line'], ['Rectangle']]
# if the pattern doesnot exist
output = []

# my list 
test = ['Line', 'Text', 'Image', 'Text', 'Line', 'Image', 'Text', 'Line', 'Rectangle']
#output and input for splitting is 
input = ['Image','Text', 'Line']
output = [['Line'], ['Text'], ['Image', 'Text', 'Line'], ['Image', 'Text', 'Line'], ['Rectangle']]
# if the pattern doesnot exist
output = []
print (test)
print (input)
result = []
l=[]
found = False
for i in input:
	if i in test:
		ind = test.index(i)+1
		ind1 = input.index(i)+1
		l.append (i)
		for m in range (ind1,len(input)-1) :
			if input[m] == test[ind]:
				l.append(input[m])
				ind += 1
				found=True
			else:
				found=False
				break
				#l= []
	if found:
		print (l)
		break