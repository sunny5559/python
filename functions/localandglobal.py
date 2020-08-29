x = 123 #global_var

def display():
	x1 = 678 #local_var
	print(x1)
	print(globals()['x'])

print(x)

z =display
z()