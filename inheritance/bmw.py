class BMW:
	def __init__(self,make,model,year):
		self.make=make
		self.model= model
		self.year =year

	def start(self):
		print("starting the car")
	def stop(self):
		print("Stopping the car")
class ThreeSeries(BMW):
	def start(self): #overrriding
		super().start()                      
		print("starting the radio")
	def __init__(self,cruiseControlledEnabled,make,model,year):
		BMW.__init__(self,make,model,year)
		self.cruiseControlledEnabled =cruiseControlledEnabled
	def display(self):
		print(self.cruiseControlledEnabled)

class FiveSeries(BMW):
	def start(self): #overridng
		print("starting the indicator")
	def __init__(self,parkingAssistEnabled,make,model,year):
		super().__init__(make,model,year)
		self.parkingAssistEnabled = parkingAssistEnabled

	def display(self):
		print(self.parkingAssistEnabled)

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