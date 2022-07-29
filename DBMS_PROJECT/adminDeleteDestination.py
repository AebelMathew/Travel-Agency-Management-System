from tkinter import *
import pymysql

def deleteDestination():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def delete():
		delquery2 = "Delete from hotels where City_ID = %s;"
		delquery = "Delete from cities where City_ID = %s;"
		delquery3 = "Delete from bus where Trans_ID = (Select Trans_ID from transport where City_ID = %s);"
		delquery4 = "Delete from train where Trans_ID = (Select Trans_ID from transport where City_ID = %s);"
		delquery5 = "Delete from airplane where Trans_ID = (Select Trans_ID from transport where City_ID = %s);"
		delquery6 = "Delete from transport where City_ID = %s;"
		data = (deleteCityID.get())
		cursor.execute(delquery2, data)
		connection.commit()
		cursor.execute(delquery3, data)
		connection.commit()
		cursor.execute(delquery4, data)
		connection.commit()
		cursor.execute(delquery5, data)
		connection.commit()
		cursor.execute(delquery6, data)
		connection.commit()
		cursor.execute(delquery, data)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Delete Destination")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	deleteCityIDLabel = Label(root, text = "City ID : ")
	deleteCityIDLabel.grid(row = 2, column = 0, pady = 0)
	deleteCityIDLabel.config(font = ("Arial", 18))
	deleteCityID=Entry(root,width=100, borderwidth=5)
	deleteCityID.grid(row=2, column=1)

	deleteButton = Button(root, text = "Delete Destination!", command = delete)
	deleteButton.grid(row = 6, column = 1, pady = 20, columnspan = 2)
	deleteButton.config(font = ("Arial", 18))