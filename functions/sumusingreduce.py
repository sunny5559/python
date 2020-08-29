from functools import reduce
lst=[5,10,15,20,25]
result =reduce(lambda x,y:x+y,lst)
print(result)