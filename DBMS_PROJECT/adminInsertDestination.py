from tkinter import *
import pymysql

def insertDestination():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def insert():
		inquery = "Insert into cities values (%s,%s,%s);"
		data = (cityID.get(),cityName.get(),countryName.get())
		cursor.execute(inquery,data)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Insert New Destination")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	cityIDLabel = Label(root, text = "City ID : ")
	cityIDLabel.grid(row = 2, column = 0, pady = 0)
	cityIDLabel.config(font = ("Arial", 18))
	cityID=Entry(root,width=100, borderwidth=5)
	cityID.grid(row=2, column=1)

	cityNameLabel = Label(root, text = "City Name : ")
	cityNameLabel.grid(row = 3, column = 0, pady = 0)
	cityNameLabel.config(font = ("Arial", 18))
	cityName=Entry(root,width=100, borderwidth=5)
	cityName.grid(row=3, column=1)

	countryNameLabel = Label(root, text = "Country Name : ")
	countryNameLabel.grid(row = 4, column = 0, pady = 0)
	countryNameLabel.config(font = ("Arial", 18))
	countryName=Entry(root,width=100, borderwidth=5)
	countryName.grid(row=4, column=1)

	insertButton = Button(root, text = "Insert!", command = insert)
	insertButton.grid(row = 6, column = 1, pady = 20, columnspan = 2)
	insertButton.config(font = ("Arial", 18))

	root.mainloop();