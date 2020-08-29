import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='test')
if conn.is_connected():
	print("connected to mysql db")
cursor = conn.cursor()

cursor.execute('select * from emp')

#row= cursor.fetchone()
rows = cursor.fetchall()

print('total num,ber of records',cursor.rowcount)
for row in rows:
	print(row)
	
cursor.close()
conn.close()