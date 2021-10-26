
count(1)
thislist.append("asdadasds")
thislist.extend(tropical)
newlist = ['hello' for x in fruits]

list1 = [10, 20, 30, 40, 50]
# start = list's size
# stop = -1
# step = -1

# reverse a list
for i in range(len(list1) - 1, -1, -2):
    print(list1[i], end=" ")
# Output 50 40 30 20 10

# class ComplexNumber:
#     def __init__(self, r=0, i=0):
#         self.real = r
#         self.imag = i

#     def get_data(self):
#         print(f'{self.real}+{self.imag}j')


# # Create a new ComplexNumber object
# num1 = ComplexNumber(2, 3)

# # Call get_data() method
# # Output: 2+3j
# num1.get_data()

# # Create another ComplexNumber object
# # and create a new attribute 'attr'
# num2 = ComplexNumber(5)
# num2.attr = 10

# # Output: (5, 0, 10)
# print((num2.real, num2.imag, num2.attr))

# # but c1 object doesn't have attribute 'attr'
# # AttributeError: 'ComplexNumber' object has no attribute 'attr'
# #print(num1.attr)