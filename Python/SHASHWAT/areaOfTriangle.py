import math
a = int(input("Enter 1st side of triangle "))
b = int(input("Enter 3rd side of triangle "))
c = int(input("Enter 2nd side of triangle "))

s=(a+b+c)/2
x = s*(s-a)*(s-b)*(s-c)
area = x**0.5
#area = math.sqrt( x )

print("area of triangle is: ", area)