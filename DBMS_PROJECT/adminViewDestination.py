from tkinter import *
import pymysql

def viewDestination():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()
	retrieve = "Select * from cities"
	cursor.execute(retrieve)
	rows = cursor.fetchall()
	i = 0

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "View Destinations Available")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	countryName = Label(root, text = "Country")
	countryName.grid(row = 2, column = 2, pady = 10, columnspan = 1)
	countryName.config(font = ("Arial", 16))

	CityName = Label(root, text = "City")
	CityName.grid(row = 2, column = 1, pady = 10, columnspan = 1)
	CityName.config(font = ("Arial", 16))

	cityId = Label(root, text = "City Id")
	cityId.grid(row = 2, column = 0, pady = 10, columnspan = 1)
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
	quitButton.grid(row = 20, column = 0, pady = 20, columnspan = 3)
	quitButton.config(font = ("Arial", 18))

	root.mainloop();