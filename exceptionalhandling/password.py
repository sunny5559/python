#defining the user defined exception

class InvalidPasswordException(Exception):
	message = "password is less than 8 characters"

	#test
try:
	password= input("enetr a password")
	if(len(password)<=8):raise InvalidPasswordException
except InvalidPasswordException as obj:
	print(obj.message)
	print("password must be atleast 9 characters")
else:
	print("valid password entered successfully")