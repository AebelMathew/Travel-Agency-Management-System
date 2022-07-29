from tkinter import *
import pymysql

def viewHotel():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()
	retrieve = "Select * from hotels"
	cursor.execute(retrieve)
	rows = cursor.fetchall()
	i = 0

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))


	windowHeading = Label(root, text = "View Hotels Available")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	hotelId = Label(root, text = "Hotel Id")
	hotelId.grid(row = 2, column = 0, pady = 10, columnspan = 1)
	hotelId.config(font = ("Arial", 16))

	hotelName = Label(root, text = "Hotel Name")
	hotelName.grid(row = 2, column = 1, pady = 10, columnspan = 1)
	hotelName.config(font = ("Arial", 16))

	price = Label(root, text = "Price")
	price.grid(row = 2, column = 2, pady = 10, columnspan = 1)
	price.config(font = ("Arial", 16))

	cityId = Label(root, text = "City Id")
	cityId.grid(row = 2, column = 3, pady = 10, columnspan = 1)
	cityId.config(font = ("Arial", 16))

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 15)
			e.grid(row = 3 + i, column = j, padx = 1, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		i += 1

	connection.commit()
	connection.close()

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 20, column = 1, pady = 20, columnspan = 2)
	quitButton.config(font = ("Arial", 18))

	root.mainloop();