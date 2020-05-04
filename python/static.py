class Tax:
    visitor=0
    NOTAX=0
    TAX_F=500000
    TAX_M=300000
    @staticmethod
    def getT(taxable,gender):
        if taxable == False:
            return Tax.NOTAX
        if gender == 'F':
            return Tax.TAX_F
        if gender == 'M':
            return Tax.TAX_M
        return Tax.NOTAX

class Student(Tax):
    def __init__(self):
        Tax.visitor+=1
    def calculateTax(self):
        self.taxable=False
        self.gender='M'
        print("student goes to college", Tax.getT(self.taxable,self.gender))
	
class Engineer(Tax):
    def __init__(self):
        Tax.visitor+=1
    def calculateTax(self):
        self.taxable=True
        self.gender='M'
        print("Engineer goes to work", Tax.getT(self.taxable,self.gender))

class HomeMaker(Tax):
    def __init__(self):
        Tax.visitor+=1
    def calculateTax(self):
        self.taxable=True
        self.gender='F'
        print("Homemaker goes nowhere", Tax.getT(self.taxable,self.gender))

s = Student()

s.calculateTax()
e = Engineer()
e.calculateTax()
h = HomeMaker()
h.calculateTax()
print(Tax.visitor)