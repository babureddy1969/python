import sqlite3
db=sqlite3.connect('student.db')
db.rollback()
def createTable():
	try:        
		cur =db.cursor()
		cur.execute('''CREATE TABLE student (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT (20) NOT NULL,
		age INTEGER,
		marks REAL);''')
		print ('table created successfully')
	except Exception as e:
		print ('error in operation',e)
		db.rollback()

	#db.close()

def insertData(student):
	qry="insert into student (name, age, marks) values(?,?,?);"
	try:
		cur=db.cursor()
		cur.execute(qry, student)
		db.commit()
		print ("student added successfully")
	except Exception as e:
		print ("error in operation",e)
		db.rollback()

def insertBatch(students):
	qry="insert into student (name, age, marks) values(?,?,?);"
	#students=[('Amar', 18, 70), ('Deepak', 25, 87)]
	try:
		cur=db.cursor()
		cur.executemany(qry, students)
		db.commit()
		print ("records added successfully")
	except Exception as e:
		print ("error in operation",e)
		db.rollback()
def readData(inp = None):
	sql="SELECT * from student "
	cur=db.cursor()
	if inp != None:
		if isinstance(inp,int):
			inp = str(inp)
			sql += " where id = ?" 
		else:
			sql += " where name like ?"
		cur.execute(sql,inp)
	else:
	    cur.execute(sql)
	while True:
		record=cur.fetchone()
		if record==None:
			break
		print (record)
		return record
	#students=cur.fetchall()
	#for rec in students:
	#print (rec)
def searchData(inp):
	sql="SELECT * from student where name like ?"
	cur=db.cursor()
	cur.execute(sql,[inp])
	while True:
		record=cur.fetchone()
		if record==None:
			break
		print (record)
	#students=cur.fetchall()
	#for rec in students:
	#print (rec)
def editData(student):
	qry="update student set name = ?, age=?, marks=? where id=?;"
	try:
		cur=db.cursor()
		cur.execute(qry, student)
		db.commit()
		print("record updated successfully")
	except Exception as e:
		print("error in operation",e)
		db.rollback()
	
def deleteData(id):
	qry="DELETE from student where id=?;"
	try:
		cur=db.cursor()
		cur.execute(qry, (id))
		db.commit()
		print("record deleted successfully")
	except Exception as e:
		print("error in operation",e)
		db.rollback()
	
def displayMenu():
	print("1. Add data")
	print("2. Edit data")
	print("3. Delete data")
	print("4. Search data")
	print("5. Display data")
	print("6. Search data")
	return input()
def readUserInput():
	inp = input ("Name, Age, marks:")
	return inp.split(',')
		
while True:
	choice = displayMenu()
	if choice == '1':
		insertData(readUserInput())
	elif choice == '2':
		id = input ("Enter id to edit: ")
		id = int(id)
		rec = readData(id)
		inp = input (rec)
		if inp:
			data = ( [ x for x in inp.split(',')]+[id] )
			editData(data)
	elif choice == '3':
		inp = input ("Enter id to delete:")
		deleteData(inp)
	elif choice == '4':
		inp = input ("Enter name to search:")
		readData([inp])
	elif choice == '5':
		readData()
	elif choice == '6':
		inp = input ("Enter name to search:")
		searchData(inp)
	else:
		break
	