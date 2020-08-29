try:
	num= int(input("enter a even number :"))
	assert num%2==0,"you have enetered a invalid input or odd number"
except AssertionError as obj:
	print (obj)
	
print("after the assertion")