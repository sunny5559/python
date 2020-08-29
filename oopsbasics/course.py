#parameterized constructors
class Course:
	def __init__(self,name,ratings):
		self.name = name
		self.ratings = ratings

c1 = Course("java Course",[1,2,3,4,5])
print(c1.name)
print(c1.ratings)

c2 =Course("java web series",[5,5,5,5])
print(c2.name)
print(c2.ratings)