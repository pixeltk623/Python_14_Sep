# # Write a Python program to get the Factorial number of given number

# num = int(input("Enter a number to find Factorial:  "))

# if num <= 0:
#     print("Factorial of entered number is not possible")
# else:
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact * i
#     print("Factorial of ",num," is ", fact)



# #  Write a Python program to get the Fibonacci series of given range    0 1 1 2 3 5

# num = int(input("Enter a number to find the Fibonacci series till:  "))
# print("")
# first = 0
# second = 1
# fib = 0
# print("Fibonacci series till ",num,"th position is: ",first, second, end=" ")
# for i in range(0,num-2):
#     fib = first + second
#     print(fib, end=" ")
#     first = second
#     second = fib


# # Write python program that swap two number with temp variable and
# # without temp variable

# num1 = int(input("Enter the first number:  "))
# num2 = int(input("Enter the second number:  "))
# print("Numbers before swap: ",num1,"  ",num2)

# # swap using 3rd variable
# x = num1
# num1 = num2
# num2 = x
# print("Numbers after swap: ",num1,"  ",num2)

# # swap without using variable
# num1 = num1 + num2
# num2 =  num1 - num2
# num1 = num1 - num2
# print("Numbers after swap: ",num1,"  ",num2)

# # Write a Python program to find whether a given number is even or odd,
# # print out an appropriate message to the user

# num = int(input("Enter any number:  "))
# if num <=0 :
#     print("You entered an invalid number.")
# elif num%2==0:
#     print("The number is even.")
# else:
#     print("number is odd.")


# # Write a Python program that compute the area of following
# # 1) Triangle (accepts base and height)2) Circle (accept radius)

# base = int(input("Enter base of triangle: "))
# height = int(input("Enter height of triangle: "))
# area = 0.5 * base * height
# print("Area of triangle is: ", area,"unit sq.")

# rad = int(input("Enter the radius of circle: "))

# area = 3.14 * rad * rad
# print("Area of circle is: ", area,"unit sq.")

# #  Write a Python program to test whether a passed letter is a vowel or not

# alpha = input("Enter any Alphabet of english: ")

# if alpha == "A" or alpha =="E" or alpha =="I" or alpha =="O" or alpha =="U" or alpha =="a" or alpha =="e" or alpha =="i" or alpha =="o" or alpha =="u":
#     print("Alphabet entered is Vovel")
# else:
#     print("You entered a consonant")


# # Write a Python program to sort three integers without using
# # conditional statements and loops.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# a1 = min(num1, num2, num3)
# a3 = max(num1, num2, num3)
# a2 = (num1 +num2+ num3) - a1 - a3
# print("Numbers in sorted order: ", a1, a2, a3)



# # Write a Python program that accepts an integer (n) and computes the value of
# # n+nn+nnn.

# num = int(input("Enter any positive number:  "))
# ans = num + num**2 + num**3
# print("Value of n + n*n + n*n*n is ",ans)


# # Write a Python program to sum of three given integers.
# # However, if two values are equal sum will be zero.

# num1 = int(input("Enter the first number:  "))
# num2 = int(input("Enter the second number:  "))
# num3 = int(input("Enter the third number:  "))

# if num1 == num2 or num2 == num3 or num3 == num1:
#     print(0)
# else:
#     print("Sum is ",num1+num2+num3)


# # Write a Python program that will return true if the two given integer
# # values are equal or their sum or difference is 5.

# num1 = int(input("Enter the first number:  "))
# num2 = int(input("Enter the second number:  "))

# if num1 == num2 or (num1+num2)==5 or (num1-num2)==5:
#     print(True)
# else:
#     print(False)


# #  Write a python program to sum of the first n positive integers

# num = int(input("Enter a number to find sum:  "))
# sum=0
# for i in range(1,num+1):
#     sum += i
# print("Sum of ",num,"natural numbers is ",sum)

# # print reverse of a number
# num = int(input("Enter a number to reverse:  "))
# revNum = 0
# while num>0:
#     rem = num%10
#     revNum = (revNum * 10) + rem
#     num= num//10
# print(revNum)

# # sum of digits
# num = int(input("Enter a number:  "))
# x=num
# sum = 0
# while num>0:
#     rem = num%10
#     sum = sum + rem
#     num = num//10
# print("Sum of digits of ",x,"is ",sum)


# # find exponent 
# num = int(input("Enter a number:  "))
# exp = int(input("Enter 2 for square and 3 for cube: "))

# if exp==2:
#     ans = num*num
#     print("Square of ", num,"is ", ans)
# elif exp==3:
#     ans =num*num*num
#     print("Cube of ", num,"is ", ans)
# else:
#     print("Input Invalid")



# # .Write a Python program to calculate the length of a string.

# text =   input("Enter a string:  ")

# print("Length of entered string is :  ",len(text))


# # Write a Python program to count the number of characters (character frequency) 
# # in a string

# text = input("Enter a string:  ")
# count = 0
# for x in text:
#     count+= 1
# print("Total number of characters in",text,"are",  count)


# # Write a Python program to count occurrences of a substring in a string

# str = input("Enter a string:  ")
# check = input("Enter a sub-string to check:  ")

# print("Number of times",check,"occured in entered string is:  ",str.count(check))


# # Write a Python program to add 'ing' at the end of a given string
# # (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead 
# # If the string length of the given string is less than 3, leave it unchanged

# str = input("Enter a string:  ")
# length = len(str)

# if length>2:
#     if str[-3:] =='ing':
#         str += 'ly'
#     else:
#         str += 'ing'

# print("--",str,"--")


# # Write a Python function that takes a list of words and returns the length of the longest one.

# testList = ["java","cpp","python"]

# lengthList = []

# for x in testList:
#     lengthList.append(len(x))

# lengthList.sort()
# # print(lengthList)
# print("Length of the longest word in",testList,"is ",lengthList[-1])

# # Write a Python function to reverses a string if it's length is a multiple of 4

# str = input("Enter a string:  ")
# length = len(str)

# if (length%4) == 0:
#     print("Reversed string of",str,"is",str[::-1])
# else:
#     print(str)


# # Write a Python program to get a string made of the first 2 and the last 2 chars
# # from a given a string. If the string length is less than 2, return instead of the empty string.

# str = input("Enter a string:  ")
# length = len(str)

# if length<2:
#     print("_____")
# else:
#     print(str[:2]+str[-2:])


# # remove all the repetations of rahul in the tuple

# newTuple = ("shravan","rahul","kavita","nisha","farook","rahul","rahul","rahul","rahul")

# newList = list(newTuple)
# List = []
# for x in range(len(newList)):
#     if newList[x] != "rahul":
#         List.append(newList[x])
# print(tuple(List))


# # find the numbers present in the list divisible by a given number

# newList = [10,4,3,16,28,36,93]

# num = int(input("Enter a number to check divisiblity:  "))
# List = []
# for x in range(len(newList)):
#     if newList[x]%num == 0:
#         List.append(newList[x])
# print(List)


# # The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
# # The list after removing duplicates : [1, 3, 5, 6]

# newList = [1, 3, 5, 6, 3, 5, 6, 1]

# List1 = []

# for i in range(len(newList)):
#     if newList[i] not in List1:
#         List1.append(newList[i])

# print(List1)