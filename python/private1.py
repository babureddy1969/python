#class declaration
class College:
	sum_of_feedback = 0.0
	#constructor with default values
	def __init__(self, name="Unknown"):
		self.visitorName = name

	def welcomeMessage(self):
		print("Hello %s , Welcome to the College" % self.visitorName)

	def averageFeedback(self):
		#average feedback is hided for the the child class
		self.__avg_feedback = College.sum_of_feedback/RateCollege.total_num_feedback
		print("Average feedback : ", self.__avg_feedback)

class RateCollege(College):
	total_num_feedback = 0
	def __init__(self, name,feedback):
		# feedback (1-10) : 1 is the best.
		self.feedback = feedback # Public Attribute

		self._staffRating = 50
		self.__collegeGuideRating = 100 # Private Attribute
		self.updateStaffRating() # update Staff rating based on feedback
		self.updateGuideRating() # update Guide rating based on feedback
		College.sum_of_feedback += self.feedback
		RateCollege.total_num_feedback += 1
		super().__init__(name)

		def printRating(self):
			print("Thanks %s for your feedback" % self._visitorName)
		
	def updateStaffRating(self):
		""" update Staff rating based on visitor feedback"""
		if self.feedback < 5 :
			self._staffRating += 5
		else:
			self._staffRating -= 5

	def updateGuideRating(self):
		""" update Guide rating based on visitor feedback"""
		if self.feedback < 5 :
			self.__collegeGuideRating += 10
		else:
			self.__collegeGuideRating -= 10
class Test:
	def __init__(self):
		# inheritance is not required for accessing class attribute
		print("sum_of_feedback (College class attribute) : ", College.sum_of_feedback)
		print("total_num_feedback (RateCollege class attribute) : ", RateCollege.total_num_feedback)
			
def main():
	## create object of class Jungle
	r = RateCollege("Ram", 3)
	r = RateCollege("Sham", 2)

	r.averageFeedback() # Average feedback : 2.5
	w = Test()
	
if __name__=='__main__':
	main()