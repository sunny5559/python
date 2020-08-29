import re
str= "take 1 up one 1-3-2020 idea  at one  time"

result= re.search(r'o\w\w',str)
result2=re.findall(r'o\w\w',str)
print(result.group())
print(result2)

result3=re.match(r't\w\w',str)
print(result3.group())

result2=re.findall(r'o\w\w',str)
print(result.group())

r = re.split(r'\d',str)
print(r)

p = re.sub(r'one','zero',str)
print(p)

re=re.findall(r'o\w+',str)
print(re)
'''
re=re.findall(r'o\w{2}',str)
print(re)

re=re.findall(r'o\w{1,2}',str)
print(re)


result =re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)
'''
result= re.search(r'^o\w\w',str)
print(result)