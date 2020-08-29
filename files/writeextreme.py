#THIS OPEN THE FILE FOE WRITING
f = open("myfile.txt","w")
print("ENTER TEXT (TYPE $ WHEN YOU ARE DONE)")
s = ''

while s != '$':
	s = input()
	f.write(s)
	
f.close()