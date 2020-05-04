# importing csv module 
import csv 

# csv file name 
filename = "student.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

def showRows():
# printing the field names 
	print(', '.join(field for field in fields)) 
	s="------------\n"
	for row in rows: 
		# parsing each column of a row 
		for col in row: 
			s+=' ' + str(col)
		s += "\n"
	print(s,'\n') 
def filterRows(dict={"name":""}):
# printing the field names 
	print(', '.join(field for field in fields)) 
	s="------------\n"
	for row in rows: 
		# parsing each column of a row 
		for col in row: 
			s+=' ' + str(col)
		s += "\n"
	print(s,'\n') 

showRows()
filterRows()
