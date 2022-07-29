from tkinter import *
import pymysql

def insertHotel():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def insert():
		inquery = "Insert into hotels values (%s,%s,%s,%s);"
		data = (hotelID.get(),hotelName.get(),price.get(),cityID.get())
		cursor.execute(inquery,data)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Insert New Hotel")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	hotelIDLabel = Label(root, text = "Hotel ID : ")
	hotelIDLabel.grid(row = 2, column = 0, pady = 0)
	hotelIDLabel.config(font = ("Arial", 18))
	hotelID=Entry(root,width=100, borderwidth=5)
	hotelID.grid(row=2, column=1)

	hotelNameLabel = Label(root, text = "Hotel Name : ")
	hotelNameLabel.grid(row = 3, column = 0, pady = 0)
	hotelNameLabel.config(font = ("Arial", 18))
	hotelName=Entry(root,width=100, borderwidth=5)
	hotelName.grid(row=3, column=1)

	priceLabel = Label(root, text = "Price : ")
	priceLabel.grid(row = 4, column = 0, pady = 0)
	priceLabel.config(font = ("Arial", 18))
	price=Entry(root,width=100, borderwidth=5)
	price.grid(row=4, column=1)

	cityIDLabel = Label(root, text = "City ID : ")
	cityIDLabel.grid(row = 5, column = 0, pady = 0)
	cityIDLabel.config(font = ("Arial", 18))
	cityID=Entry(root,width=100, borderwidth=5)
	cityID.grid(row=5, column=1)

	insertButton = Button(root, text = "Insert!", command = insert)
	insertButton.grid(row = 6, column = 1, pady = 20, columnspan = 2)
	insertButton.config(font = ("Arial", 18))

	root.mainloop();