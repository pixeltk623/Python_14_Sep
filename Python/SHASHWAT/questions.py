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


# # print a value multiple times in same tuple

# newTuple = (1,2,3)
# n = int(input("Enter how many times you want to duplicate the tuple:  "))
# finalTuple = (newTuple * n)

# print(finalTuple)


# # I1.Write a Python program to get a single string from two given strings, 
# # separated by a space and swap the first two characters of each string.

# str1 = input("Enter first string:  ")
# str2 = input("Enter second string: ")

# newStr2 = str1[:2]+str2[2:]
# newStr1 = str2[:2]+str1[2:]

# print(newStr1," ", newStr2)


# # B7.Write a Python program to count the occurrences of each word in a given sentence

# str = 'the quick brown fox jumps over the lazy dog.'
# counts = dict()
# words = str.split()

# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1

# print(counts)


# # I3.Write a Python program to find the first appearance of the substring 'not'
# # and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' 
# # substring with 'good'. Return the resulting string.

# def not_poor(str1):
#     snot = str1.find('not')
#     spoor = str1.find('poor')

#     if spoor > snot and snot>0 and spoor>0:
#         str1 = str1.replace(str1[snot:(spoor+4)], 'good')
#         print(str1)
#     else:
#         print(str1)

# not_poor('The lyrics is not that poor!')
# not_poor('The lyrics is poor!')


# # A2.Write a Python program to get a string from a given string where all occurrences 
# # of its first char have been changed to '$', except the first char itself

# str = input("Enter a string:  ")
# char = str[0]  
# length = len(str)  
# str = str.replace(char, '$')  
# str = char + str[1:]  
  
# print(str)


# # A3. Write a Python function to insert a string in the middle of a string.

# str = input("Enter a string:  ")
# str1 = input("Enter string to insert:  ")

# x = int(len(str)/2)

# print(str[:x+1]+" " + str1 + str[(x+1):])


# # B5. Write a Python function to get the largest number ,
# # smallest num and sum of all from a list

# def largeNum(numList):
#     maxNum = numList[0]

#     for x in numList:
#         if x > maxNum:
#             maxNum = x
#     return maxNum

# def smallNum(numList):
#     smNum = numList[0]

#     for x in numList:
#         if x < smNum:
#             smNum = x
#     return smNum

# def sumOfNum(numList):
#     sum = 0
#     for x in numList:
#         sum += x
#     return sum    

# numList = [5,44,31,7,551,24,2]
# print(numList)
# print("Largest number in the list is: ",largeNum(numList))
# print("Largest number in the list is: ",smallNum(numList))
# print("Sum of all numbers in the list is: ",sumOfNum(numList))


# # I1. Write a Python program to count the number of strings where the 
# # string length is 2 or more and the first and last character are same from a
# # given list of strings.

# charList = ['abc', 'xyz', 'aba', '1221']

# count = 0

# for x in charList: 
#     if len(x)>1 and x[0]==x[1]:
#         count+=1
# print(count)


# # I2.Write a Python program to remove duplicates from a list

# myList = ["Yellow","Blue","Brown","Blue","Green","Yellow"]

# print(myList)

# mySet = list(set(myList))

# print(mySet)


# # I3.Write a Python program to check a list is empty or not.

# myList = []

# if not myList:
#     print("List is empty")


# # I4.Write a Python function that takes two lists and returns True if they have at least one common member

# def listCheck(list1,list2):
#     for x in list1:
#         for y in list2:
#             if x==y:
#                 return True

# list1 = [1,2,3,4,5]
# list2 = [7,8,9,4,5]
# list3 = [7,8,9,0]

# print(listCheck(list1,list2))
# print(listCheck(list1,list3))


# # I5.Write a Python program to generate and print a list of first and last 5 elements 
# # where the values are square of numbers between 1 and 30

# squareList = []

# for i in range(1,31):
#     if i>5 and i<=25:
#         continue
#     else:
#         squareList.append(i**2)

# print(squareList)


# # I6. Write a Python function that takes a list and returns a new list with 
# # unique elements of the first list

# myList = [1,1,2,2,1,3,44,2,1,5,7,9,3,41,8,6,32]
# newList = []

# for x in myList:
#     if x not in newList:
#         newList.append(x)

# print(newList)


# # I7. Write a Python program to convert a list of characters into a string

# charList = ["a","b","c","d","e","f","g"]
# str = "".join(charList)
# print(str)


# # A1.Write a Python program to select an item randomly from a list.

# import random
# myList = [1,2,4,3,55,77,99,5,44,85]
# print(myList)

# print(random.choice(myList))


# # A2.Write a Python program to find the second smallest number in a list.

# myList = [55,77,99,5,44,85,1,2,4,3]

# myList.sort()

# print("Smallest number in list is:  ",myList[0])


# # A4.Write a Python program to check whether a list contains a sublist

# test_list = [5, 6, 3, 8, 2, 1, 7, 1]

# print("The original list : " + str(test_list))

# sublist = [8, 2, 1]

# res = False
# for idx in range(len(test_list) - len(sublist) + 1):
# 		if test_list[idx : idx + len(sublist)] == sublist:
# 			res = True
# 			break
		
# print("Is sublist present in list ? : " + str(res))


# # A4.Write a Python program to check whether a list contains a sublist

# def is_Sublist(List, subList):
# 	sub_set = False
# 	if subList == []:
# 		sub_set = True
# 	elif subList == List:
# 		sub_set = True
# 	elif len(subList) > len(List):
# 		sub_set = False

# 	else:
# 		for i in range(len(List)):
# 			if List[i] == subList[0]:
# 				n = 1
# 				while (n < len(subList)) and (List[i+n] == subList[n]):
# 					n += 1
				
# 				if n == len(subList):
# 					sub_set = True

# 	return sub_set

# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))


# # A5.Write a Python program to split a list into different variables.

# myList = ["Black", "Blue", "Brown"]

# var1,var2,var3 =myList

# print(var1,var2,var3)


# # B2.Write a Python program to create a tuple with different data types

# myTuple = ("String",True,2.1452,1)

# print(myTuple)


# # B3. Write a Python program to create a tuple with numbers

# myTuple = 5,4,6,2,1,9

# print(myTuple)


# # B4.Write a Python program to convert a tuple to a string

# myTuple = ('m','y','T','u','p','l','e')

# str1 = ''.join(myTuple)

# print(str1)


# # B5.Write a Python program to check whether an element exists within a tuple

# myTuple = ('m','y','T','u','p','l','e')

# print("l" in myTuple)
# print("a" in myTuple)


# # B7.Write a Python program to find the length of a tuple.

# myTuple = ('m','y','T','u','p','l','e')

# print("length of tuple is",len(myTuple))


# # B6.Write a Python program to convert a list to a tuple

# myTuple = ('m','y','T','u','p','l','e')

# myList = list(myTuple)

# print(myList)


# # I1. Write a Python program to reverse a tuple

# tuple1 = ("myTuple")

# tuple2 = reversed(tuple1)

# print("Reversed tuple is ",tuple(tuple2))


# # I2.Write a Python program to replace last value of tuples in a list

# myList = [(2,1,9),(5,4,6)]

# print([myTuple[:-1] + (10,) for myTuple in myList])


# # I3.Write a Python program to find the repeated items of a tuple

# myTuple = (5,4,6,2,1,9,4,6,2,2,1,9,4,6)

# print(myTuple.count(2))


# # A1.Write a Python program to remove an empty tuple(s) from a list of tuples.

# myList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# myList = [Tuple for Tuple in myList if Tuple]
# print(myList)


# # A2.Write a Python program to unzip a list of tuples into individual lists

# myList = [(2,1),(5,4),(6,9)]
# print(list(zip(*myList)))


# # A3. Write a Python program to convert a list of tuples into a dictionary

# myList = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# dict1 = {}
# for a, b in myList:
#     dict1.setdefault(a, []).append(b)
# print (dict1)


