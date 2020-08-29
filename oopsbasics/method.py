#define instance method
#parameterized constructors
from builtins import sum
class Course:
	def __init__(self,name,ratings):
		self.name = name
		self.ratings = ratings
	
	def average(self):
		numberOfRatings= len(self.ratings)
		average = sum(self.ratings)/numberOfRatings
		print("average ratings for",self.name,"IS",average)

c1 = Course("java Course",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 =Course("java web series",[5,5,5,5])
print(c2.name)
print(c2.ratings)
c2.average()