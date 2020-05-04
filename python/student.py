import sqlite3
db=sqlite3.connect('student.db')

def addStudent(name, age, marks):
    sql = "insert into student (name,age,marks) values (?,?,?)"
    print(sql)
    cur = db.cursor()
    cur.execute(sql,(name,age,marks))
    db.commit()

def readStudent(id=None,sortBy={'name':'desc'}):
    sql = "select * from student"
    cur = db.cursor()
    if id:
        sql += " where id = ?"
        result = cur.execute(sql,(id,))
    else:
        result = cur.execute(sql)
    print(sql)
    rows = result.fetchall()
    keys = list(sortBy.keys())
    values = list(sortBy.values())
    print(keys,values)
    if keys[0] == 'name' and values[0] == 'desc':
        rows = sorted(rows,key=lambda x:x[1],reverse=True)
    elif keys[0] == 'name' and values[0] == 'asc':
        rows = sorted(rows,key=lambda x:x[1])
    elif keys[0] == 'marks' and values[0] == 'asc':
        rows = sorted(rows,key=lambda x:x[3])
    elif keys[0] == 'marks' and values[0] == 'desc':
        rows = sorted(rows,key=lambda x:x[3],reverse=True)
    elif keys[0] == 'age' and values[0] == 'asc':
        rows = sorted(rows,key=lambda x:x[2])
    elif keys[0] == 'age' and values[0] == 'desc':
        rows = sorted(rows,key=lambda x:x[2],reverse=True)
    print(rows)
    # for row in rows:
    #     print(row)

def updateStudent(id, name, age, marks):
    sql = "update student set name=?,age=?,marks=? where id=?"
    print(sql, name, age, marks, id)
    try:
        cur = db.cursor()
        cur.execute(sql,[name,age,marks,id])
        db.commit()
        print("Success")
    except Exception as e:
        print(e)

def delStudent(id):
    sql = "delete from student where id=?"
    print(sql)
    cur = db.cursor()
    cur.execute(sql,(id,))
    db.commit()

# addStudent('Raj',20, 400)
# addStudent('suraj',19, 300)
# addStudent('Sumanth',18, 350)
#updateStudent(1, 'Raj Kumar',19,500)
#delStudent(1)
#readStudent(None,{'age':'asc'})
