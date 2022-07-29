from tkinter import *
import pymysql

def insertTransport():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def insert():
		inquery = "Insert into transport values (%s,%s,%s);"
		data = (transportID.get(),Type.get(),cityID.get())
		data2 = (transportID.get(),price.get(),provider.get())
		cursor.execute(inquery,data)
		connection.commit()
		if(Type.get() == "BUS"):
			inquery2 = "Insert into bus values (%s,%s,%s);"
		elif(Type.get() == "TRAIN"):
			inquery2 = "Insert into train values (%s,%s,%s);"
		else:
			inquery2 = "Insert into airplane values (%s,%s,%s);"
		cursor.execute(inquery2,data2)
		connection.commit()
		connection.close()
		root.destroy()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 4)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Insert New Transport")
	windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 2)
	windowHeading.config(font = ("Arial", 22))

	transportIDLabel = Label(root, text = "Transport ID : ")
	transportIDLabel.grid(row = 2, column = 0, pady = 0)
	transportIDLabel.config(font = ("Arial", 18))
	transportID=Entry(root,width=100, borderwidth=5)
	transportID.grid(row=2, column=1)

	TypeLabel = Label(root, text = "Type : ")
	TypeLabel.grid(row = 3, column = 0, pady = 0)
	TypeLabel.config(font = ("Arial", 18))
	Type=Entry(root,width=100, borderwidth=5)
	Type.grid(row=3, column=1)

	cityIDLabel = Label(root, text = "City ID : ")
	cityIDLabel.grid(row = 4, column = 0, pady = 0)
	cityIDLabel.config(font = ("Arial", 18))
	cityID=Entry(root,width=100, borderwidth=5)
	cityID.grid(row=4, column=1)

	priceLabel = Label(root, text = "Price : ")
	priceLabel.grid(row = 5, column = 0, pady = 0)
	priceLabel.config(font = ("Arial", 18))
	price=Entry(root,width=100, borderwidth=5)
	price.grid(row=5, column=1)

	providerLabel = Label(root, text = "Provider : ")
	providerLabel.grid(row = 6, column = 0, pady = 0)
	providerLabel.config(font = ("Arial", 18))
	provider=Entry(root,width=100, borderwidth=5)
	provider.grid(row=6, column=1)

	insertButton = Button(root, text = "Insert!", command = insert)
	insertButton.grid(row = 7, column = 1, pady = 20, columnspan = 2)
	insertButton.config(font = ("Arial", 18))

	root.mainloop();