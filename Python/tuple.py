# newTuple = ("sharvan", "rahul", "kavita" , "nisha", "farook")

# print(newTuple)

# print(type(newTuple))

# print(len(newTuple))


# constructTuple = tuple(("sharvan", "rahul", "kavita", "nisha", "farook"))

# print(constructTuple)

# print(type(constructTuple))

# print(newTuple[1]) # rahul
# print(newTuple[-1]) # farook
# print(newTuple[1:4]) # "rahul", "kavita", "nisha" ,"farook" ||  "kavita", "nisha",  "rahul", 
# # || "rahul", "kavita", "nisha", "farook" || "rahul", "kavita", "nisha",
# print(newTuple[-4:-2]) # "rahul", | "rahul", "kavita", "nisha",  | "rahul", "kavita",
# print(newTuple[:2]) # "sharvan", "rahul", | "sharvan", "rahul", "kavita"  || 
# print(newTuple[3:]) #  "farook" ||  "farook"  || "nisha", "farook"
# print(newTuple[-4:]) # "rahul", "kavita" , "nisha", "farook"


# # rahul
# # farook


# ('rahul', 'kavita', 'nisha')
# ('rahul', 'kavita')
# ('sharvan', 'rahul')
# ('nisha', 'farook')
# ('rahul', 'kavita', 'nisha', 'farook')



newTuple = ("sharvan", "rahul", "kavita" , "nisha", "farook","rahul","rahul","rahul")

# print("rahul" in newTuple)


# if "rahasdaul" in newTuple:
# 	print("Yes")	


# newList = list(newTuple)

# newList[1] = "Amit"

# #print(newList)

# finalTuple = tuple(newList)

# print(finalTuple)
# count = 0
# for x in range(len(newTuple)):
# 	if newTuple[x]=='rahul':
# 		count = count + 1


# print(count)

# list2 = [5,8,9,7]

# newList = []

# for x in list2:
	
# 	if x!=8:
# 		newList.append(x)


# print(newList)


# lsit1 = [1, 3, 5, 6, 3, 5, 6, 1]

# print(set(lsit1))


# newList =  [1, 3, 5, 6, 3, 5, 6, 1]
      
# list1=[]
# for x in newList:
#     if x not in list1:
#         list1.append(x)
#         # print(x)
      
# print(list1)

#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")

#Define a function to show a message
def myclick():
   message= "Hello "+ entry.get()
   label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
   entry.delete(0, 'end')
   label.pack(pady=30)

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
entry = ttk.Entry(frame, width= 40)
entry.insert(INSERT, "Enter Your Name")
entry.pack()
#Create a Button
ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
win.mainloop()
