a=[1,2,3,4,5]
b=[2,4,6,12,5]

result =[]
'''for i in a:
	if i in b:
		result.append(i)
print(result)
'''

result = [i for i in a if i in b]
print(result)