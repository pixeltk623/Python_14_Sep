# # class Employee():
	
# # 	da = 0
# # 	hra = 0
# # 	ca = 0
# # 	medical = 0
# # 	covid = 5000
# # 	pt = 200
# # 	tax = 0
# # 	pf = 0
# # 	baseSalary = 0

# # 	# ---- Earning -------------------#
# # 	def __init__(self, name, baseSalary):
# # 		self.name = name
# # 		self.baseSalary = baseSalary
# # 	def dearnessAllowance(self):
# # 		self.da = int(self.baseSalary)*0.1
# # 		return self.da

# # 	def hraAllowance(self):
# # 		self.hra = int(self.baseSalary)*0.25
# # 		return self.hra
# # 	def cAllowance(self):
# # 		self.ca = int(self.baseSalary)*0.05
# # 		return self.ca
# # 	def medicalAllowance(self):
# # 		self.medical = int(self.baseSalary)*0.025
# # 		return self.medical

# # 	# ---- Earning End -------------------#

# # 	# ---- Deducation Start -------------------#

# # 	def taxes(self):
# # 		if int(self.baseSalary)>=20000:
# # 			self.tax = int(self.baseSalary)*0.025
# # 		elif int(self.baseSalary)>=30000:
# # 			self.tax = int(self.baseSalary)*0.045
# # 		elif int(self.baseSalary)>=40000:
# # 			self.tax = int(self.baseSalary)*0.07
# # 		else:
# # 			self.tax = 0

# # 		return self.tax

# # 	def calculatePf(self):
# # 		if int(self.baseSalary)>=20000:
# # 			self.pf = int(self.baseSalary)*0.09
# # 		else:
# # 			self.pf = 0

# # 		return self.pf

# # 	def earningSalary(self):

# # 		#return (int(self.baseSalary) + self.da + self.hra + self.ca + self.medical + self.covid)

# # 		return (int(self.baseSalary) + self.dearnessAllowance() + self.hraAllowance() + self.cAllowance() + self.medicalAllowance() + self.covid)


# # 	def deducationSalaryCal(self):

# # 		return (self.calculatePf()+self.taxes()+self.pt)

# # 	def calculateGrossSalary(self):
# # 		return self.earningSalary() + self.deducationSalaryCal()

# # 	def takeHomeSalary(self):
# # 		return self.calculateGrossSalary() - self.deducationSalaryCal()

# # name = input("Enter Your Name: ")
# # baseSalary = input("Base Salary: ")

# # objectT = Employee(name, baseSalary)

# # print("Earning", objectT.earningSalary())
# # print("Deducation", objectT.deducationSalaryCal())
# # print("Gross", objectT.calculateGrossSalary())
# # print("Take Home", objectT.takeHomeSalary())

# # # print(objectT)
# # # objectT.setMyName(name)

# # # objectT.getMyName()

# class Employee:
	

# 	__dept = "IT"

# 	def __init__(self, name="Test", email = "test@gmail.com", Salary = "54546"):
# 		self.name = name
# 		self.email = email
# 		self.Salary = Salary

# 	def __str__(self):
# 		#return {self.name}

# 		return f'Details({self.name} {self.email} {self.Salary})'

# 	def __getDept(self):
# 		return self.__dept

# 	def newDept(self):
# 		return self.__getDept()



# objectT = Employee("Sharvan")

# print(objectT.newDept())

# # objectT1 = Employee()

# # objectT2 = Employee("Sharvan")

# # objectT3 = Employee()

# # print(objectT)
# # print(objectT1)
# # print(objectT2)
# # print(objectT3)

# Super Class
class Company():
	def __int__(self, name):
		self.name = name

	def getCompanyName(self):
		return "Tops Tech"
#

class Employee(Company):
	def __init__(self, name):
		super(Company, self).__init__()
		self.name = name

	def childFunction(self):
		return "Hello This is Child Function"
		

objectT = Employee("Kumar")

print(objectT.getCompanyName())
print(objectT.childFunction())