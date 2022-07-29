from tkinter import *
from adminViewHotel import *
from adminInsertHotel import *
from adminDeleteHotel import *

def displayHotel():
	root = Tk()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 2)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Edit Hotels Available")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	viewHotelListLabel = Label(root, text = "View Hotels : ")
	viewHotelListLabel.grid(row = 2, column = 0, pady = 10)
	viewHotelListLabel.config(font = ("Arial", 18))
	viewHotelListButton = Button(root, text = "GO!", command = viewHotel)
	viewHotelListButton.grid(row = 2, column = 1, pady = 10)
	viewHotelListButton.config(font = ("Arial", 18))

	insertNewHotelLabel = Label(root, text = "Insert New Hotels : ")
	insertNewHotelLabel.grid(row = 3, column = 0, pady = 10)
	insertNewHotelLabel.config(font = ("Arial", 18))
	insertNewHotelButton = Button(root, text = "GO!", command = insertHotel)
	insertNewHotelButton.grid(row = 3, column = 1, pady = 10)
	insertNewHotelButton.config(font = ("Arial", 18))

	deleteHotelLabel = Label(root, text = "Delete Hotels : ")
	deleteHotelLabel.grid(row = 4, column = 0, pady = 10)
	deleteHotelLabel.config(font = ("Arial", 18))
	deleteHotelButton = Button(root, text = "GO!", command = deleteHotel)
	deleteHotelButton.grid(row = 4, column = 1, pady = 10)
	deleteHotelButton.config(font = ("Arial", 18))

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 5, column = 0, pady = 20, columnspan = 2)
	quitButton.config(font = ("Arial", 18))

	root.mainloop()