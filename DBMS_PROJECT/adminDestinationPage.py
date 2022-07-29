from tkinter import *
from adminViewDestination import *
from adminDeleteDestination import *
from adminInsertDestination import *

def displayDestination():
	root = Tk()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 2)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Edit Destinaitons Available")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	viewDestinationListLabel = Label(root, text = "View Destinations : ")
	viewDestinationListLabel.grid(row = 2, column = 0, pady = 10)
	viewDestinationListLabel.config(font = ("Arial", 18))
	viewDestinationListButton = Button(root, text = "GO!", command = viewDestination)
	viewDestinationListButton.grid(row = 2, column = 1, pady = 10)
	viewDestinationListButton.config(font = ("Arial", 18))

	insertNewDestinationLabel = Label(root, text = "Insert New Destinations : ")
	insertNewDestinationLabel.grid(row = 3, column = 0, pady = 10)
	insertNewDestinationLabel.config(font = ("Arial", 18))
	insertNewDestinationButton = Button(root, text = "GO!", command = insertDestination)
	insertNewDestinationButton.grid(row = 3, column = 1, pady = 10)
	insertNewDestinationButton.config(font = ("Arial", 18))

	deleteDestinationLabel = Label(root, text = "Delete Destinations : ")
	deleteDestinationLabel.grid(row = 4, column = 0, pady = 10)
	deleteDestinationLabel.config(font = ("Arial", 18))
	deleteDestinationButton = Button(root, text = "GO!", command = deleteDestination)
	deleteDestinationButton.grid(row = 4, column = 1, pady = 10)
	deleteDestinationButton.config(font = ("Arial", 18))

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 5, column = 0, pady = 20, columnspan = 2)
	quitButton.config(font = ("Arial", 18))

	root.mainloop()