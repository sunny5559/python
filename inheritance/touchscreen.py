from abc import abstractmethod,ABC
class TouchScreeNlaptop(ABC):
	def __init__(self,make):
		self.make = make

	@abstractmethod
	def scroll(self):
		pass
	@abstractmethod
	def click(self):
		pass

class HP(TouchScreeNlaptop):
	def __init__(self,make):
		super().__init__(make)

	def scroll(self):
		print("scrolling the hp")

class DELL(TouchScreeNlaptop):
	def __init__(self,make):
		super().__init__(make)

	def scroll(self):
		print("scrolling the DELL")

class HPNOTEBOOK(HP):
	def __init__(self,make,model):
		super().__init__(make)
		self.model= model

	def click(self):
		print("clicking the hp")

class DELLNOTEBOOK(DELL):
	def __init__(self,make,model):
		super().__init__(make)
		self.model= model

	def click(self):
		print("clicking the DELL")

hpx = HPNOTEBOOK("HP","HPNOTEBOOK 2020")
print(hpx.make,hpx.model)
hpx.scroll()
hpx.click()

dx= DELLNOTEBOOK("DELL","Dellnotebook 2020")
print(dx.make,dx.model)
dx.scroll()
dx.click()