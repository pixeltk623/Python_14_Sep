
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# print(x)
# print(y)
# print(z)

# x = y = z = 5


# x,y,x = 5,8,9


# print(x)
# print(y)
# print(z)


# x = 5
# print("Python is " , x)

# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# a = 1 + 2 + 3 + \
#     4 + 5 + 6 + \
#     7 + 8 + 9

# print(a)

# a = "Hello, World!"
# print(a[1])

# print("h" in a)

# print(len(a))
# for x in a:
# 	print(x)

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[2:])

# b = " Hello, World! "
# print(b[-5:-2])

# print(b.lower())

# print(b.strip())

# c = b.replace("H","J")

# print(c)

# a = "Hello,World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# class ClassName(object):
# 	"""docstring for ClassName"""
# 	age = 10

# 	def greet(self):

# name = "Kumar"
# age = 24

# txt = "My name is {} and age is {}";

# print(txt.format(name,age))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))


# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))


# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))


# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
