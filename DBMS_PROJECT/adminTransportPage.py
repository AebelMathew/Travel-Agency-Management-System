from tkinter import *
from adminViewTransport import *
from adminInsertTransport import *
from adminDeleteTransport import *

def displayTransport():
	root = Tk()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 2)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Edit Transports Available")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	viewTransportListLabel = Label(root, text = "View Transports : ")
	viewTransportListLabel.grid(row = 2, column = 0, pady = 10)
	viewTransportListLabel.config(font = ("Arial", 18))
	viewTransportListButton = Button(root, text = "GO!", command = viewTransport)
	viewTransportListButton.grid(row = 2, column = 1, pady = 10)
	viewTransportListButton.config(font = ("Arial", 18))

	insertNewTransportLabel = Label(root, text = "Insert New Transports : ")
	insertNewTransportLabel.grid(row = 3, column = 0, pady = 10)
	insertNewTransportLabel.config(font = ("Arial", 18))
	insertNewTransportButton = Button(root, text = "GO!", command = insertTransport)
	insertNewTransportButton.grid(row = 3, column = 1, pady = 10)
	insertNewTransportButton.config(font = ("Arial", 18))

	deleteTransportLabel = Label(root, text = "Delete Transports : ")
	deleteTransportLabel.grid(row = 4, column = 0, pady = 10)
	deleteTransportLabel.config(font = ("Arial", 18))
	deleteTransportButton = Button(root, text = "GO!", command = deleteTransport)
	deleteTransportButton.grid(row = 4, column = 1, pady = 10)
	deleteTransportButton.config(font = ("Arial", 18))

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 5, column = 0, pady = 20, columnspan = 2)
	quitButton.config(font = ("Arial", 18))

	root.mainloop()