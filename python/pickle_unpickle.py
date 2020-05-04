#SERIALIZATION

import pickle
filename='student.dat'
d = {'id':1,'name':'Ram','age':20,'marks':300}

outfile = open(filename,'wb')
pickle.dump(d,outfile)
outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)