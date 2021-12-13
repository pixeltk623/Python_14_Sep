from tkinter import *
import mysql.connector
import tkinter.messagebox as m

def dbConn():
	conn = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "",
		database = "tkinter_python"
	)
	return conn


def saveUser():
	inputName = nameE.get()
	inputEmail = emailE.get()
	inputMobile = mobileE.get()

	# if inputMobile=='':
	# 	m.showinfo("Message", "Mobile can Not be blank")
	# elif len(inputMobile)<10:
	# 	m.showinfo("Message", "Required")

	if inputName=='':
		m.showinfo("Message", "Name can Not be blank")

	if inputEmail=='':
		m.showinfo("Message", "Email can Not be blank")

	if inputMobile=='':
		m.showinfo("Message", "Mobile can Not be blank")

	if inputName!='' and inputEmail!='' and inputMobile!='':
		conn =  dbConn()
		myCursor = conn.cursor()
		query = "INSERT INTO `users`(`name`, `email`, `mobile`) VALUES ('"+inputName+"','"+inputEmail+"','"+inputMobile+"')"
		myCursor.execute(query)
		conn.commit()
		m.showinfo("Message", "User Created")
	else:
		m.showinfo("Message", "Error")
crud = Tk()

crud.geometry("500x500")
crud.title("CRUD")
crud.configure(bg="lightblue")

name = Label(crud, text="Name")
name.place(x=100,y=20)

email = Label(crud, text="Email")
email.place(x=100, y=60)

mobile = Label(crud, text="Mobile")
mobile.place(x=100, y=100)


nameE = Entry()
nameE.place(x=160,y=20)

emailE = Entry()
emailE.place(x=160, y=60)

mobileE = Entry()
mobileE.place(x=160, y=100)

button = Button(crud, text="Save", bg="green", command = saveUser)
button.place(x=140, y=140)


mainloop()

