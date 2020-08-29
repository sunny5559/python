#implementation of encapsulation

class Student:
	def setId(self,id):  #@ Reserved assignment
		self.id = id
	def getId(self):
		return self.id
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name


s = Student()
s.setId(123)
s.setName("mj")
print(s.getId())
print(s.getName())