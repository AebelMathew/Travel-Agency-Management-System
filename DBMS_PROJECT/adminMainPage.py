from tkinter import *
from adminDestinationPage import *
from adminHotelPage import *
from adminTransportPage import *

def adminDisplay():
	root = Tk()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 2)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Main Page - Admin")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	changeDestinationListLabel = Label(root, text = "Edit Destinations : ")
	changeDestinationListLabel.grid(row = 2, column = 0, pady = 10)
	changeDestinationListLabel.config(font = ("Arial", 18))
	changeDestinationListButton = Button(root, text = "GO!", command = displayDestination)
	changeDestinationListButton.grid(row = 2, column = 1, pady = 10)
	changeDestinationListButton.config(font = ("Arial", 18))

	changeHotelListLabel = Label(root, text = "Edit Hotels : ")
	changeHotelListLabel.grid(row = 3, column = 0, pady = 10)
	changeHotelListLabel.config(font = ("Arial", 18))
	changeHotelListButton = Button(root, text = "GO!", command = displayHotel)
	changeHotelListButton.grid(row = 3, column = 1, pady = 10)
	changeHotelListButton.config(font = ("Arial", 18))

	changeTransportListLabel = Label(root, text = "Edit Transports : ")
	changeTransportListLabel.grid(row = 4, column = 0, pady = 10)
	changeTransportListLabel.config(font = ("Arial", 18))
	changeTransportListButton = Button(root, text = "GO!", command = displayTransport)
	changeTransportListButton.grid(row = 4, column = 1, pady = 10)
	changeTransportListButton.config(font = ("Arial", 18))

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 5, column = 0, pady = 20, columnspan = 2)
	quitButton.config(font = ("Arial", 18))

	root.mainloop()