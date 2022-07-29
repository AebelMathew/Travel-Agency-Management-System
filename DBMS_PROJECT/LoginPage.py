from tkinter import *
from adminMainPage import *
from userCityPage import *
import pymysql

def displayLoginPage():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def checkLogin():
		customer = False
		loggedIn = False
		retrieve = "Select Customer_ID, Password_Customer from customer;"
		cursor.execute(retrieve)
		row = cursor.fetchall()
		connection.commit()

		for r in row:
			if(r[0] == username.get()):
				if(r[1] == password.get()):
					customer = True
					loggedIn = True
					retrieve3 = "Select First_Name, Last_Name from personal_info where Customer_ID = %s;"
					data = (username.get())
					cursor.execute(retrieve3,data)
					names = cursor.fetchall()
					x = username.get()
					root.destroy()
					userDisplayCity(names[0][0] + " " + names[0][1], x)
					break

		if(not customer):
			retrieve2 = "Select Admin_ID, Password_Admin from admin;"
			cursor.execute(retrieve2)
			row = cursor.fetchall()
			connection.commit()

			for r in row:
				if(r[0] == username.get()):
					if(r[1] == password.get()):
						loggedIn = True
						root.destroy()
						adminDisplay()

		connection.close()

		if(not loggedIn):
			errorLabel = Label(root, text = "Username and Password do not match!!!")
			errorLabel.grid(row = 4, column = 0, pady = 10, columnspan = 3)
			errorLabel.config(font = ("Arial", 18))

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "LOGIN")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	usernameLabel = Label(root, text = "USERNAME:  ")
	usernameLabel.grid(row = 2, column = 0, pady = 10)
	usernameLabel.config(font = ("Arial", 18))
	username=Entry(root,width=100, borderwidth=5)
	username.grid(row=2, column=1)
	username.insert(0,"")

	passwordLabel = Label(root, text = "PASSWORD: ")
	passwordLabel.grid(row = 3, column = 0, pady = 10)
	passwordLabel.config(font = ("Arial", 18))
	password=Entry(root,width=100, borderwidth=5,show="*")
	password.grid(row=3, column=1)
	password.insert(0,"")

	loginButton = Button(root, text = "Login", command = checkLogin)
	loginButton.grid(row = 5, column = 0, pady = 10, columnspan = 3)
	loginButton.config(font = ("Arial", 18))


	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 6, column = 0, pady = 20, columnspan = 3)
	quitButton.config(font = ("Arial", 18))

	root.mainloop()