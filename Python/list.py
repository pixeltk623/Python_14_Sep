# 1. ordered
# 2. Allow to change
# 3. Allow Duplicate values


# listOfName = ["Dhruv", "Nandini", "Namita", "Shashwat", "Sharvan"]



# print(listOfName)
# print(type(listOfName))
# print(len(listOfName))


# print(listOfName[3])


# for x in listOfName:
# 	print(x)


# for x in range(len(listOfName)):
# 	print(listOfName[x])


# for x in range(len(listOfName)):
# 	if x%2!=0:
# 		print(listOfName[x])


# listOfName = list(("Dhruv", "Nandini", "Namita", "Shashwat", "Sharvan"))

# print(listOfName)

listOfName = ["Dhruv", "Nandini", "Namita", "Shashwat", "Sharvan","Namita", "Shashwat", "Sharvan"]

# print(listOfName[2]) # // Namita
# print(listOfName[-2])   # Shashwat
# print(listOfName[2:5])  # "Namita", "Shashwat", "Sharvan","Namita"
# print(listOfName[:3])  # "Shashwat", "Sharvan","Namita", "Shashwat", "Sharvan"
# print(listOfName[3:])  # "Shashwat", "Sharvan","Namita", "Shashwat", "Sharvan"
# print(listOfName[-4:-1])  #  "Sharvan","Namita", "Shashwat", "Sharvan"


# Namita
# Shashwat
# ['Namita', 'Shashwat', 'Sharvan']

# ['Dhruv', 'Nandini', 'Namita']

# ['Shashwat', 'Sharvan', 'Namita', 'Shashwat', 'Sharvan']

# ['Sharvan', 'Namita', 'Shashwat']


#print(len(listOfName))

# newList = []

# for x in range(len(listOfName)):

# 	if x%2!=0:
# 		listOfName[x] = "Test"
# 		newList.append(listOfName[x])
# 		# print()
# 	else:
# 		newList.append(listOfName[x])


# print(newList)
# for x in range(len(listOfName)):
# 	pass


# a = Car
# b = acr

# newString = "Hello This is Sharvan Kumar"

# newList = []
# count = 0
# for x in newString.lower():
# 	if x=='a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
# 		count = count + 1
# 		newList.append(x)
# 		#print(x)

# print(count)
# print(newList)

# list1 = [2,4]

# list2 = [8,10]


# print(list1+list2)
# list1.extend(list2)
# print(list1)

# list2.extend(list1)

# print(list2)

# print(list1==list2)	

# exit()

# str1 = "Car"
# str2 = "cRAr"

# a = sorted(str1)

# print(a)

# str1New = str1.lower()
# str2New = str2.lower()


# if len(str1New)==len(str2New):
	
# 	sortedString1 = sorted(str1New)
# 	sortedString2 = sorted(str2New)

# 	# print(sortedString1)
# 	# print(sortedString2)

# 	if sortedString1==sortedString2:
# 		print("Yes")

# else:
# 	print("Not")


listOfName = ["Dhruv", "Nandini", "Namita", "Shashwat", "Sharvan","Namita", "Shashwat", "Sharvan", "Nandini"]



# listOfName[1] = "Test"

# print(listOfName)


# listOfName[1:5] = ["Test","Test1","Test2","Test4"]

# print(listOfName)


# listOfName.insert(1, "Test")

# print(listOfName)


# listOfName.pop()

# print(listOfName)

# listOfName.pop(0)

# print(listOfName)

# listOfName.remove("Nandini")
# listOfName.remove("Nandini")

# print(listOfName)

# listOfName.clear()

# del listOfName

# print(listOfName)

# listOfName.remove(1)

# print(listOfName)


# print("Nandini" in listOfName)

# newList = []

# for x in range(len(listOfName)):
# 	if listOfName[x]=='Nandini':
# 		pass
# 		#listOfName.remove("Nandini")
# 		#print(listOfName[x])
# 	else:
# 		newList.append(listOfName[x])

# print(newList)

# def sort(nums):
# 	for i in range(len(nums)-1,0,-1):
# 		#print(nums[i])
# 		for j in range(i):
# 			#print(j)
# 			if nums[j]>nums[j+1]:
# 				temp = nums[j]
# 				nums[j] = nums[j+1]
# 				nums[j+1] = temp

# nums = [5,3,8,6,7,2]
# sort(nums)

# print(nums)
# 	


# thislist = ["sharvan", "dixit", "renis", "devin", "sonali"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)


# thislist = ["sharvan", "dixit", "renis", "devin", "sonali"]
# thislist.sort(reverse=True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)


# thislist = ["Sharvan", "dixit", "renis", "devin", "sonali"]
# thislist.sort()
# print(thislist)

# thislist = ["Sharvan", "dixit", "renis", "devin", "sonali"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["Sharvan", "dixit", "renis", "devin", "sonali"]
# thislist.reverse()
# print(thislist)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# thisTuple = ("Sharvan", "dixit", "renis", "devin", "sonali","Sharvan", "dixit")

# print(thisTuple)



# A set is a collection which is unordered, unchangeable, and unindexed.


# myset = {"Sharvan", "dixit", "renis", "devin", "sonali","Sharvan", "dixit"}

# print(myset)

# thisset.add("Sharvan")
# thisset.update(tropical)
# thisset.update(mylist)
# thisset.remove("dixit")
# thisset.discard("renis")
# x = thisset.pop()
# thisset.clear()
# del thisset


# set3 = set1.union(set2)

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# set1.update(set2)

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# x.intersection_update(y)

# z = x.intersection(y)

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# x.symmetric_difference_update(y)

# z = x.symmetric_difference(y)


# A dictionary is a collection which is ordered, changeable and does not allow duplicates.


# x = thisdict.get("name")
# x = thisdict.keys()
# x = thisdict.values()
# x = thisdict.items()
# thisdict.update({"name": "kumar"})
# thisdict.pop("name")
# thisdict.popitem()
# del thisdict["name"]
# thisdict.clear()
# mydict = thisdict.copy()



