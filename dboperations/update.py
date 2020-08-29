import mysql.connector;

def update(id):
	conn = mysql.connector.connect(host='localhost',database='mydb',user='root',password='test')

	if conn.is_connected():
		print("connected to mysql db")
		cursor = conn.cursor()
		str = "UPDATE emp SET name ='dj'WHERE id='%d'"
		args=(id)

		try:
			cursor.execute(str % args)
			conn.commit()
			print("record updated")
		except:
			conn.rollback()

		finally:
			cursor.close()
			conn.close()

empId= int(input('enter the employee id'))
update(empId)