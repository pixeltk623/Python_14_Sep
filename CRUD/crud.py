import mysql.connector

class Employee:
	__serverName = "localhost"
	__userName = "root"
	__password = ""
	__dbName = "python_14_sep"
	conn = None

	def __init__(self):
		self.dbConnect()

	def dbConnect(self):
		self.conn = mysql.connector.connect(
			host = self.__serverName,
			user = self.__userName,
			password = self.__password,
			database = self.__dbName 
		)
		return self.conn

	def insertData(self,name,email,mobile,gender):
		myCursor = self.conn.cursor()
		query = "INSERT INTO employee (name, email, mobile, gender) VALUES ('"+name+"','"+email+"','"+mobile+"','"+gender+"')"
		myCursor.execute(query)
		self.conn.commit()
		return True

	def getAllData(self):
		myCursor = self.conn.cursor()
		query = "SELECT * FROM employee ORDER BY name DESC"
		myCursor.execute(query)
		myresult = myCursor.fetchall()

		return {"data" : myresult}

	def getDataById(self, id):
		myCursor = self.conn.cursor()
		query = "SELECT * FROM employee WHERE id = "+str(id)
		myCursor.execute(query)
		myresult = myCursor.fetchone()
		return {"data" : myresult}

	def deleteById(self, eid):
		myCursor = self.conn.cursor()
		query = "DELETE FROM employee WHERE id = "+str(eid)
		myCursor.execute(query)
		self.conn.commit()
		return {"status" : True}

	def updateDataById(self,data,uid):
		myCursor = self.conn.cursor()
		query = "UPDATE employee SET name = '"+data['name']+"', email = '"+data['email']+"', mobile = '"+data['mobile']+"', gender = '"+data['gender']+"' WHERE id = "+str(uid)
		myCursor.execute(query)
		self.conn.commit()
		return {"status" : True}

# name = input("Enter Your Name: ")
# email = input("Enter Your Email: ")
# mobile = input("Enter Your Mobile: ")
# gender = input("Enter Your Gender: ")
# data = {"name" : name, "email" : email, "mobile" : mobile, "gender" : gender}

objectT = Employee()

print("---------------------CRUD------------------")
print("1. INSERT")
print("2. GET All Records")
print("3. GET")
print("4. UPDATE")
print("5. DELETE")

c = int(input("Enter Your Choice: "))

if c==1:
	name = input("Enter Your Name: ")
	email = input("Enter Your Email: ")
	mobile = input("Enter Your Mobile: ")
	gender = input("Enter Your Gender: ")
	objectT.insertData(name,email,mobile,gender)

elif c==2:
	dataAll = objectT.getAllData()
	print(dataAll)
elif c==3:
	uid = input("Enter Your Id: ")
	dataOne = objectT.getDataById(uid)
	print(dataOne)
elif c==4:
	uid = input("Enter Your Id: ")
	name = input("Enter Your Name: ")
	email = input("Enter Your Email: ")
	mobile = input("Enter Your Mobile: ")
	gender = input("Enter Your Gender: ")
	data = {"name" : name, "email" : email, "mobile" : mobile, "gender" : gender}
	updateById = objectT.updateDataById(data, uid)
	print(updateById)
elif c==5:
	uid = input("Enter Your Id: ")
	deleteOne = objectT.deleteById(uid)
	print(deleteOne)
else:
	print("Not Selected")



