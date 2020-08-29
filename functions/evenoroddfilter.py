lst= [1,2,3,3,5,6,7,8,9,97,34,5]

result = list(filter(lambda x:x%2==0,lst))
print(result)

for i in result:print(i)