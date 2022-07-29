from tkinter import *
import pymysql

def displayFinalFail():
	root = Tk()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Transaction Failed!!! Please try again!")
	windowHeading.grid(row = 1, column = 0, pady = 30, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 2, column = 0, pady = 20, columnspan = 3)
	quitButton.config(font = ("Arial", 18))