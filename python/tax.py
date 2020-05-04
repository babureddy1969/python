from abc import ABCMeta, abstractmethod
class Tax(metaclass=ABCMeta):

    @staticmethod
    def getT(taxable,gender):
        if taxable == False:
            return 0
        if gender == 'F':
            return 500000
        if gender == 'M':
            return 300000
        return 0
    def __init__(self):
        self.__tax=0
        self.__tax_m=300000
        self.__tax_f=500000
    @abstractmethod
    def calculateTax(self):
        print("")

    def getTaxBracket(self,o):
        if o.taxable == False:
            return self.__tax
        if o.gender == 'M':
            return self.__tax_m
        elif o.gender == 'F':
            return self.__tax_f

class Student(Tax):
    def calculateTax(self):
        self.taxable=False
        self.gender='M'
        print("student goes to college", self.getTaxBracket(self),Tax.getT(self.taxable,self.gender))
	
class Engineer(Tax):
    def calculateTax(self):
        self.taxable=True
        self.gender='M'
        print("Engineer goes to work", self.getTaxBracket(self))

class HomeMaker(Tax):
    def calculateTax(self):
        self.taxable=True
        self.gender='F'
        print("Homemaker goes nowhere", self.getTaxBracket(self))

s = Student()

s.calculateTax()
e = Engineer()
e.calculateTax()
h = HomeMaker()
h.calculateTax()
