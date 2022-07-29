from tkinter import *
import pymysql

def deleteTransport():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def delete():
		delquery2 = "Delete from bus where Trans_ID = %s;"
		delquery3 = "Delete from train where Trans_ID = %s;"
		delquery4 = "Delete from airplane where Trans_ID = %s;"
		delquery = "Delete from transport where Trans_ID = %s;"
		data = (deleteTransportID.get())
		cursor.execute(delquery2, data)
		connection.commit()
		cursor.execute(delquery3, data)
		connection.commit()
		cursor.execute(delquery4, data)
		connection.commit()
		cursor.execute(delquery, data)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Delete Transport")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	deleteTransportIDLabel = Label(root, text = "Transport ID : ")
	deleteTransportIDLabel.grid(row = 2, column = 0, pady = 0)
	deleteTransportIDLabel.config(font = ("Arial", 18))
	deleteTransportID=Entry(root,width=100, borderwidth=5)
	deleteTransportID.grid(row=2, column=1)

	deleteButton = Button(root, text = "Delete Transport!", command = delete)
	deleteButton.grid(row = 6, column = 1, pady = 20, columnspan = 2)
	deleteButton.config(font = ("Arial", 18))