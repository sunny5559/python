import logging

logging.basicConfig(filename="mylog.log",level = logging.DEBUG)
try:
	f = open("myfile.txt","w")
	a,b = [int(x) for x in input("enter two numbers").split()]
	logging.info("division in progress")
	c = a/b
	f.write("writing %d into the file" %c)
except :
	print("Division by zero is not allowed")
	print("please enter a non zero number")
	logging.error("Division by zero")
else:
	print("you have entered non zero number")
finally:
	f.close()
	print("file is closed")
print("code after the exception")
