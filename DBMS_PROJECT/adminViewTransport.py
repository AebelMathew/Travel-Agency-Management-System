from tkinter import *
import pymysql

def viewTransport():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()
	retrieve = "Select  bus.Provider, bus.Cost, transport.Type, transport.City_ID from bus inner join transport on bus.Trans_ID = transport.Trans_ID"
	retrieve1 = "Select train.Provider, train.Cost, transport.Type, transport.City_ID from train inner join transport on train.Trans_ID = transport.Trans_ID"
	retrieve2 = "Select airplane.Provider, airplane.Cost, transport.Type, transport.City_ID from airplane inner join transport on airplane.Trans_ID = transport.Trans_ID"
	cursor.execute(retrieve)
	rows = cursor.fetchall()
	i = 0
	k = 0
	l = 0

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "View Transports Available")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 4)
	windowHeading.config(font = ("Arial", 22))

	provider = Label(root, text = "Provider")
	provider.grid(row = 2, column = 0, pady = 10, columnspan = 1)
	provider.config(font = ("Arial", 16))

	cost = Label(root, text = "Cost")
	cost.grid(row = 2, column = 1, pady = 10, columnspan = 1)
	cost.config(font = ("Arial", 16))

	Type = Label(root, text = "Type")
	Type.grid(row = 2, column = 2, pady = 10, columnspan = 1)
	Type.config(font = ("Arial", 16))

	cityId = Label(root, text = "City Id")
	cityId.grid(row = 2, column = 3, pady = 10, columnspan = 1)
	cityId.config(font = ("Arial", 16))

	for r in rows:
		for j in range(len(r)):
			e = Entry(root, width = 25)
			e.grid(row = 3 + i, column = j, padx = 1, pady = 10, columnspan = 1)
			e.insert(0, r[j])
		i += 1

	cursor.execute(retrieve1)
	rows = cursor.fetchall()

	for r in rows:
		for j in range(len(r)):
			e1 = Entry(root, width = 25)
			e1.grid(row = 10 + k, column = j, padx = 1, pady = 10, columnspan = 1)
			e1.insert(0, r[j])
		k += 1

	cursor.execute(retrieve2)
	rows = cursor.fetchall()

	for r in rows:
		for j in range(len(r)):
			e1 = Entry(root, width = 25)
			e1.grid(row = 20 + l, column = j, padx = 1, pady = 10, columnspan = 1)
			e1.insert(0, r[j])
		l += 1

	connection.commit()
	connection.close()

	quitButton = Button(root, text = "Quit!", command = root.destroy)
	quitButton.grid(row = 100, column = 0, pady = 20, columnspan = 4)
	quitButton.config(font = ("Arial", 18))

	root.mainloop();