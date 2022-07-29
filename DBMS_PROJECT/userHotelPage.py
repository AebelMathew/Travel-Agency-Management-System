from tkinter import *
import pymysql
from userTransportPage import *

def userDisplayHotels(name, customerID, CityID):
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def goToTransport(name, customerID, CityID, HotelID, NumOfRooms):
		root.destroy()
		userDisplayTransports(name, customerID, CityID, HotelID, NumOfRooms)


	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Welcome, " + name)
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	HotelListLabel = Label(root, text = "Choose The Hotel You Want To Stay In : ")
	HotelListLabel.grid(row = 2, column = 0, pady = 10, columnspan = 3)
	HotelListLabel.config(font = ("Arial", 18))

	retrieve = "Select Hotel_ID, Hotel_Name, Price from hotels where City_ID = %s;"
	data = (CityID)
	cursor.execute(retrieve,data)
	rows = cursor.fetchall()
	i = 0

	price = Label(root, text = "Price (per room)")
	price.grid(row = 3, column = 2, pady = 10, columnspan = 1)
	price.config(font = ("Arial", 16))

	hotelName = Label(root, text = "Hotel Name")
	hotelName.grid(row = 3, column = 1, pady = 10, columnspan = 1)
	hotelName.config(font = ("Arial", 16))

	hotelId = Label(root, text = "Hotel Id")
	hotelId.grid(row = 3, column = 0, pady = 10, columnspan = 1)
	hotelId.config(font = ("Arial", 16))

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 15)
			e.grid(row = 4 + i, column = j, padx = 1, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		i += 1

	connection.commit()
	connection.close()

	enterIDLabel = Label(root, text = "Enter the Hotel ID for your desired Hotel : ")
	enterIDLabel.grid(row = 99, column = 0, pady = 10, columnspan = 2)
	enterIDLabel.config(font = ("Arial", 16))
	enterID = Entry(root, width=100, borderwidth=5)
	enterID.grid(row=99, column=2, columnspan = 1)

	NumOfRoomsLabel = Label(root, text = "Enter the Number of Rooms Required : ")
	NumOfRoomsLabel.grid(row = 100, column = 0, pady = 10, columnspan = 2)
	NumOfRoomsLabel.config(font = ("Arial", 16))
	NumOfRooms = Entry(root, width=100, borderwidth=5)
	NumOfRooms.grid(row=100, column=2, columnspan = 1)

	nextButton = Button(root, text = "Next >>", command = lambda : goToTransport(name, customerID, CityID, enterID.get(), int(NumOfRooms.get())))
	nextButton.grid(row = 101, column = 0, pady = 20, columnspan = 3)
	nextButton.config(font = ("Arial", 18))

	root.mainloop()