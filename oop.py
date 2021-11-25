import mysql.connector
class Employee():
	employeeName = "Sharvan"
	dept = "IT"
	serverName = "localhost"
	userName = "root"
	password = ""
	dbName = "cartl"

	def dbConnection(self):
		conn = mysql.connector.connect(host=self.serverName, user=self.userName,password=self.password,database=self.dbName)
		return conn

	def getAllProducts(self):
		conn = self.dbConnection()
		mycursor = conn.cursor()
		mycursor.execute("SELECT * FROM product_images")
		myresult = mycursor.fetchall()
		return myresult
		

	def getEmployeeName(self):
		print("My Name Is Sharvan Kumar")

	def getEmployeeEmail(self):
		return "s@gmail.com"

	def getDepTName(self):
		return self.dept + "Hai"

objectOfEmployee = Employee()

# objectOfEmployee.employeeName = "Rahul"

# objectOfEmployee.getEmployeeName()
# print(objectOfEmployee.getEmployeeEmail())
# print(objectOfEmployee.getDepTName())


# print(objectOfEmployee.dbConnection())

result = objectOfEmployee.getAllProducts()


print(result)