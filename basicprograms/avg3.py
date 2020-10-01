sid = int(input("Enter the student id"))
name = input("Enter student name")
sub1 = float(input("enter the marks sub1"))
sub2 = float(input("enter the marks of sub2"))
sub3 = float(input("enter the matrks of sub3"))
marks = float(sub1+sub2+sub3)
avg= marks/3
print("Student id is ",sid,"\n Student's Name is ",name,"\nStudent's Total marks scored are ",marks,"\n Average : ",avg)

#average of 3 numbers
a,b,c= [int(x) for x in input('Enter three integer numbers').split()]
avg= (a+b+c)/3
print("avg of 3",avg)
