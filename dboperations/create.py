import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='test')
if conn.is_connected():
	print("connected to mysql db")
cursor = conn.cursor()
try:
	cursor.execute("insert into emp values(3,'mj',5000)")
	conn.commit()
	print("employee added")
except:
	conn.rollback()

cursor.close()
conn.close()