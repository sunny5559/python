#abstractmethod and interface
from abc import abstractmethod,ABC
class BMW(ABC):
	
	def __init__(self,make,model,year):
		self.make=make
		self.model= model
		self.year =year
	@abstractmethod
	def start(self):
		pass
	@abstractmethod
	def stop(self):
		pass
	
	@abstractmethod
	def drive(self):
		pass	

class ThreeSeries(BMW):
	
	def start(self): #overrriding
		super().start()                      
		print("starting the radio")

	def stop(self): #overrriding
		super().stop()                      
		print("stopping the radio")
	
	
	def __init__(self,cruiseControlledEnabled,make,model,year):
		BMW.__init__(self,make,model,year)
		self.cruiseControlledEnabled =cruiseControlledEnabled
	
	def display(self):
		print(self.cruiseControlledEnabled)
	
	def drive(self):
		print("three series is  being driven")

class FiveSeries(BMW):
	
	def start(self): #overridng
		print("starting the indicator")

	def stop(self): #overrriding
		super().stop()                      
		print("stopping the indicator")
	
	
	def __init__(self,parkingAssistEnabled,make,model,year):
		super().__init__(make,model,year)
		self.parkingAssistEnabled = parkingAssistEnabled

	def display(self):
		print(self.parkingAssistEnabled)

	def drive(self):
		print("five series is  being driven")


threeSeries = ThreeSeries(True,"BMW","328i","2020")
print(threeSeries.cruiseControlledEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True,"VITARA","765i","2020")
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()

