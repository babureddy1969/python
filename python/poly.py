from abc import ABCMeta, abstractmethod
class Person(metaclass=ABCMeta):
	@abstractmethod
	def workPlace(self):
		print("")

class Student(Person):
	def workPlace(self):
		print("student goes to college")
	
class Engineer(Person):
	def workPlace(self):
		print("Engineer goes to work")

class HomeMaker(Person):
	def workPlace(self):
		pass

s = Student()
s.workPlace()
e = Engineer()
e.workPlace()
h = HomeMaker()
h.workPlace()
		
		