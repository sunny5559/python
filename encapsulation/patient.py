class Patient:
	def setId(self,id):  #@ Reserved assignment
		self.id = id
	def getId(self):
		return self.id
	def setName(self,name):
		self.name = name
	def getName(self):
		return self.name
	def setSSN(self,ssn):
		self.ssn = ssn
	def getSSN(self):
		return self.ssn
p = Patient()
p.setId(456)
p.setName("mj")
p.setSSN(26011997)
print(p.getId())
print(p.getName())
print(p.getSSN())