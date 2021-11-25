#file = open("test.txt", 'r')

# print(file.read())

# print(file.read(15))

# print(file.readline())
#print(file)

# newFile = open("fileNew.text", "w")

# newFile.write("This is Sharvan")

# newFile = open("fileNew.text", "r")

# print(newFile.read())

# newFile.close()


# newFile = open("fileNew.text", "a")

# newFile.write("New Name \n")

# newFile = open("fileNew.text", "r")

# print(newFile.read())

# import random

# for x in range(1,6):
# 	name = input("Enter The Name: ")
# 	fileName = str(random.randint(10000, 500000))+"_"+name
# 	#print(fileName)
# 	openFile = open(fileName+".txt", "w")
# 	openFile.write(fileName)
# 	openFile.close()

# 	readFile = open(fileName+".txt", 'r')
# 	print(readFile.read())
# 	readFile.close()

# import os
# #os.remove("test.txt")
# os.rmdir("New")


# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London"]
# file1.writelines(L)
# file1.close()


# newOpen = open("myfile.txt", "r")

# print(newOpen.read())

# with open("myfile.txt", "r") as file:
# 	data = file.readlines()

# 	print(data)
# 	for line in data:
# 		print(line)

# txt = "     banana     "

# x = txt.strip()

# print("of all fruits", x, "is my favorite")