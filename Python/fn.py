# def printName():
# 	print("My Name is Kumar")

# def getMyName():
# 	return "My Name is Sharvan"


# printName() # My Name is Kumar
# print(getMyName()) #

#  sum of 5 and 3 is = 8


# def addTwoNumber():
# 	x = int(input("Enter The First Number:- "))
# 	y = int(input("Enter The Second Number:- "))
	
# 	return "Sum of " + str(x) + " and "+str(y)+" is = " + str(x+y)


# z = addTwoNumber()

# print(z)

# x = a  = 5
# y = b  = 6



# def addTwoNumber(x,y):
# 	return x+y



# a = int(input("Enter The First Number:- "))
# b = int(input("Enter The Second Number:- "))

# z = addTwoNumber(a,b)

# print(z)


# def printTheNameOfUser(firstName = "Test", lastName = "Test"):
# 	print(firstName + " " + lastName)


# printTheNameOfUser() # //Test Test
# printTheNameOfUser("Sharvan") # //Sharvan Test // Sharvan Kumar // Sharvan
# printTheNameOfUser("Kumar") # // Kumar // Kumar Test // 
# printTheNameOfUser("", "Patel") # " " Patel 
# printTheNameOfUser("Patel", "Kumar") # Patel Kumar


# Test Test
# Sharvan Test
# Kumar Test
#  Patel
# Patel Kumar



# def chessBoard():
# 	for i in range(1,9):
# 		#print(i)
# 		for j in range(1,9):
# 			sumOfIJ = i+j

# 			if sumOfIJ%2==0:
# 				print("White ", end = "")
# 			else:
# 				print("Black ", end = "")
# 		print("\n")


# chessBoard()


# def getFact(n = 0):
# 	fact = 1
# 	if n<0:
# 		return 0
# 	elif n==0 or n==1:
# 		return fact
# 	else:
# 		for x in range(1, n+1):
# 			#print(x)
# 			fact = fact * x		
# 	return fact


# print(getFact(5))


# z = lambda x: x *5


# print(z(5))


# avg = lambda a,b,c,d: (a+b+c+d)/4


# print(avg(4,3,9,9))


# fullName = lambda x,y : x +" "+ y


# print(fullName("Sharvan","Kumar"))
