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