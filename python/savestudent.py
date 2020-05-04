def getInput():
    name = input("Enter Name:" )
    grade = input("Grade:")
    section = input("Enter Section:" )
    marks = input("Enter marks:" )
    city = input("Enter city:")
    return name, grade, section, marks, city
def saveData(id,name,cls, section,marks,city):
    with open('sortedstudent.csv','a') as f:
        f.write("\n{},{},{},{},{},{}".format(id,name,cls, section,marks,city))
def getId():
    with open('sortedstudent.csv') as f:
        return sorted([int(i.split(',')[0]) for i in f.readlines()[1:-1]])[-1]
def display():
    with open('sortedstudent.csv') as f:
        v = f.readlines()
        marks=[]
        for s in v[1:-1]:
            m = s.split(',')
            marks+=[(int(m[4]),int(m[0]))]
        marks = sorted(marks,reverse=True)
        print(marks)
        for m,id in marks:
            for s in v[1:-1]:
                x = s.split(',')
                if int(x[0]) == id:
                    print(s)
display()
exit(0)
while True:
    id = getId()
    name,cls, section,marks,city = getInput()
    saveData(id,name,cls,section,marks,city)
    choice = input("Do you want to continue y/n? ")
    if choice == 'n':
        break