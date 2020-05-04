#class declaration
class College:
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
	def __init__(self, feedback):
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
		print("Feedback : %s \tGuide Rating: %s \tStaff Rating: %s "
			% (self.feedback, self.__collegeGuideRating, self._staffRating))

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
def main():
	## create object of class Jungle
	j = College("Meher")
	j.welcomeMessage() # Hello Meher, Welcome to the Jungle

	r = RateCollege(8)
	r.printRating() # Feedback : 3 Guide Rating: 110 Staff Rating: 55

	r._staffRating = 30 # directly change the _staffRating
	print("Staff rating : ", r._staffRating) # Staff rating : 30
	print ("Guide rating : ", r._RateCollege__collegeGuideRating) # Guide rating : 110

if __name__=='__main__':
	main()