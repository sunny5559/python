s = '	You are awesome		'
print (s)
print(type(s))

s1 = """You are
the creator of
Your destiny"""

print(s1)
print(type(s1))

#index of a string
print(s[0])
print(s*2)

print(len(s1))
print(len(s))

#slicing

print(s[0:5])
print(s[0:])
print(s[:9])
print(s[-3:-1])

print(s[0:9:2])
print(s[15::-1])
#reverse
print(s[::-1])



#strip function
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#find function
print(s.find("awe",0,len(s)))
print(s.find("awe",0,8))
print (s.count('a'))
print(s.replace('awesome','superb'))

print(s.upper())
print(s.lower())
print(s.title())