def customgen(x,y):
	while x<y:
		yield x
		x+=1

result = customgen(32,40)

for i in result:print(i)