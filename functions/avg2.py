def average(a,b):
	print("average of two number is",(a+b)/2)

average(a=10,b=20) #keywords are used


def averagereturn(a,b):
	print(a)
	print(b)
	return (a+b)/2

print(averagereturn(b=10,a=22))

def avg(a=10,b=30):
	return (a+b)/2

print(avg()) #default values will be called