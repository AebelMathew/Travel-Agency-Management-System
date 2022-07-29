from tkinter import *
import pymysql

def deleteHotel():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def delete():
		delquery = "Delete from hotels where Hotel_ID = %s;"
		data = (deleteHotelID.get())
		cursor.execute(delquery,data)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Delete Hotel")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	deleteHotelIDLabel = Label(root, text = "Hotel ID : ")
	deleteHotelIDLabel.grid(row = 2, column = 0, pady = 0)
	deleteHotelIDLabel.config(font = ("Arial", 18))
	deleteHotelID=Entry(root,width=100, borderwidth=5)
	deleteHotelID.grid(row=2, column=1)

	deleteButton = Button(root, text = "Delete Hotel!", command = delete)
	deleteButton.grid(row = 6, column = 1, pady = 20, columnspan = 2)
	deleteButton.config(font = ("Arial", 18))