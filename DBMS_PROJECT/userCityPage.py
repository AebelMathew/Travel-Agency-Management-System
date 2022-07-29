from tkinter import *
import pymysql
from userHotelPage import *


def userDisplayCity(name, customerID):
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def goToHotels(name, customerID, CityID):
		root.destroy()
		userDisplayHotels(name, customerID, CityID)


	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Welcome, " + name)
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	DestinationListLabel = Label(root, text = "Choose The City You Want To Visit : ")
	DestinationListLabel.grid(row = 2, column = 0, pady = 10, columnspan = 3)
	DestinationListLabel.config(font = ("Arial", 18))

	retrieve = "Select * from cities"
	cursor.execute(retrieve)
	rows = cursor.fetchall()
	i = 0

	cityName = Label(root, text = "City Name")
	cityName.grid(row = 3, column = 1, pady = 10, columnspan = 1)
	cityName.config(font = ("Arial", 16))

	countryName = Label(root, text = "Country Name")
	countryName.grid(row = 3, column = 2, pady = 10, columnspan = 1)
	countryName.config(font = ("Arial", 16))

	cityId = Label(root, text = "City Id")
	cityId.grid(row = 3, column = 0, pady = 10, columnspan = 1)
	cityId.config(font = ("Arial", 16))

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 15)
			e.grid(row = 4 + i, column = j, padx = 1, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		i += 1

	connection.commit()
	connection.close()

	enterIDLabel = Label(root, text = "Enter the City ID for your desired Destination : ")
	enterIDLabel.grid(row = 99, column = 0, pady = 10, columnspan = 2)
	enterIDLabel.config(font = ("Arial", 16))
	enterID = Entry(root, width=100, borderwidth=5)
	enterID.grid(row=99, column=2, columnspan = 1)

	nextButton = Button(root, text = "Next >>", command = lambda : goToHotels(name, customerID, enterID.get()))
	nextButton.grid(row = 100, column = 0, pady = 20, columnspan = 3)
	nextButton.config(font = ("Arial", 18))

	root.mainloop()