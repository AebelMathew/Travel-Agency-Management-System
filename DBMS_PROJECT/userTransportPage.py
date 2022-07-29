from tkinter import *
import pymysql
from userBillPage import *

def userDisplayTransports(name, customerID, CityID, HotelID, NumOfRooms):
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def getBill(name, customerID, CityID, HotelID, NumOfRooms, TransportProvider, TypeOfTransport, NumOfSeats):
		root.destroy()
		displayBill(name, customerID, CityID, HotelID, NumOfRooms, TransportProvider, TypeOfTransport, NumOfSeats)


	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Welcome, " + name)
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	HotelListLabel = Label(root, text = "Choose The Transport for Going To Your Desired Location : ")
	HotelListLabel.grid(row = 2, column = 0, pady = 10, columnspan = 3)
	HotelListLabel.config(font = ("Arial", 18))

	retrieve = "Select train.Provider, train.Cost, transport.Type from train inner join transport on transport.Trans_ID = train.Trans_ID where train.Trans_ID in (Select Trans_ID from transport where City_ID = %s);"
	retrieve1 = "Select bus.Provider, bus.Cost, transport.Type from bus inner join transport on transport.Trans_ID = bus.Trans_ID where bus.Trans_ID in (Select Trans_ID from transport where City_ID = %s);"
	retrieve2 = "Select airplane.Provider, airplane.Cost, transport.Type from airplane inner join transport on transport.Trans_ID = airplane.Trans_ID where airplane.Trans_ID in (Select Trans_ID from transport where City_ID = %s);"
	data = (CityID)
	cursor.execute(retrieve,data)
	rows = cursor.fetchall()
	i = 0
	k = 0
	l = 0

	price = Label(root, text = "Price (per person)")
	price.grid(row = 3, column = 1, pady = 10, columnspan = 1)
	price.config(font = ("Arial", 16))

	provider = Label(root, text = "Provider")
	provider.grid(row = 3, column = 0, pady = 10, columnspan = 1)
	provider.config(font = ("Arial", 16))

	Type = Label(root, text = "Type")
	Type.grid(row = 3, column = 2, pady = 10, columnspan = 1)
	Type.config(font = ("Arial", 16))

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 50)
			e.grid(row = 4 + i, column = j, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		i += 1

	cursor.execute(retrieve1,data)
	rows = cursor.fetchall()

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 50)
			e.grid(row = 10 + k, column = j, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		k += 1

	cursor.execute(retrieve2,data)
	rows = cursor.fetchall()

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 50)
			e.grid(row = 20 + l, column = j, pady = 10, columnspan = 2)
			e.insert(0, r[j])
		l += 1

	connection.commit()
	connection.close()

	typeOfTransportLabel = Label(root, text = "Enter the Type of your desired mode of Transportaion : ")
	typeOfTransportLabel.grid(row = 98, column = 0, pady = 10, columnspan = 2)
	typeOfTransportLabel.config(font = ("Arial", 16))
	typeOfTransport = Entry(root, width = 100, borderwidth=5)
	typeOfTransport.grid(row=98, column=2, columnspan = 1)

	enterIDLabel = Label(root, text = "Enter the Provider for your desired mode of Transportaion : ")
	enterIDLabel.grid(row = 99, column = 0, pady = 10, columnspan = 2)
	enterIDLabel.config(font = ("Arial", 16))
	enterID = Entry(root, width = 100, borderwidth=5)
	enterID.grid(row=99, column=2, columnspan = 1)

	NumOfSeatsLabel = Label(root, text = "Enter the Number of Seats Required : ")
	NumOfSeatsLabel.grid(row = 100, column = 0, pady = 10, columnspan = 2)
	NumOfSeatsLabel.config(font = ("Arial", 16))
	NumOfSeats = Entry(root, width = 100, borderwidth=5)
	NumOfSeats.grid(row=100, column=2, columnspan = 1)

	nextButton = Button(root, text = "Get Bill >>", command = lambda : getBill(name, customerID, CityID, HotelID, NumOfRooms, enterID.get(), typeOfTransport.get(), int(NumOfSeats.get())))
	nextButton.grid(row = 101, column = 0, pady = 20, columnspan = 6)
	nextButton.config(font = ("Arial", 18))

	root.mainloop()