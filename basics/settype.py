s={10,20,30,"xyz",10,20}
print(s)
print(type(s))

s.update([55,66])
print(s)
print(type(s))

#print(s[0:6])

s.remove(30)
print(s)


f = frozenset(s)
f.update(20)