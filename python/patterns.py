seq = ['Line','Rectangle','Image','Line','Image','Rectangle','Image','Line','Rectangle']
subseq = ['Image','Line','Rectangle']
#subseq = ['Image','Line']

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

#i, n, m = -1, len(seq), len(subseq)
def matchPatterns(seq,subseq):
	i, n, m = -1, len(seq), len(subseq)
	try:
		while True:
			i = seq.index(subseq[0], i + 1, n - m + 1)
			if subseq == seq[i:i + m]:
				#print ([seq[i:i+m]])
				return seq[i:i+m]
	except ValueError:
		print (-1)
l=[]
#while subseq != []:
#	l += [matchPatterns(seq,subseq)]
#	subseq.pop()
j = 0	
for i in range(0,len(seq)-1):
	if seq[i] == subseq[j]:
		l += [seq[i]]
		j+=1
	elif seq[i] in subseq:
		l = [seq[i]] 
		j=0
print (l)	