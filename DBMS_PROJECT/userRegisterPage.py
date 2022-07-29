from tkinter import *
import pymysql

def displayRegistration():
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def insert():
		retrieve = "Select Customer_ID from personal_info order by Customer_ID desc limit 1;"
		cursor.execute(retrieve)
		row = cursor.fetchall()
		for r in row:
			customer_id = ("C" + str(int(r[0].split("C")[1]) + 1).rjust(4, "0"))
		inquery3 = "Insert into customer values (%s,%s);"
		data3 = (customer_id,password.get())
		cursor.execute(inquery3,data3)
		connection.commit()
		inquery = "Insert into personal_info values (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
		data = (customer_id,firstname.get(),lastname.get(),address.get(),sex.get(),email.get(),int(phone.get()),dob.get(),int(cardno.get()))
		cursor.execute(inquery,data)
		connection.commit()
		inquery2 = "Insert into card_info values (%s,%s,%s,%s);"
		data2 = (customer_id,int(cardno.get()),int(cvv.get()),cardname.get())
		cursor.execute(inquery2,data2)
		connection.commit()
		connection.close()
		root.destroy()
	
	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 5, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "REGISTER")
	windowHeading.grid(row = 1, column = 0, pady = 5, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	firstnameLabel = Label(root, text = "FIRST NAME: ")
	firstnameLabel.grid(row = 2, column = 0, pady = 0)
	firstnameLabel.config(font = ("Arial", 18))
	firstname=Entry(root,width=100, borderwidth=5)
	firstname.grid(row=2, column=1)

	lastnameLabel = Label(root, text = "LAST NAME: ")
	lastnameLabel.grid(row = 3, column = 0, pady = 0)
	lastnameLabel.config(font = ("Arial", 18))
	lastname=Entry(root,width=100, borderwidth=5)
	lastname.grid(row=3, column=1)

	passwordLabel = Label(root, text = "PASSWORD: ")
	passwordLabel.grid(row = 5, column = 0, pady =0)
	passwordLabel.config(font = ("Arial", 18))
	password=Entry(root,width=100, borderwidth=5,show="*")
	password.grid(row=5, column=1)

	addressLabel = Label(root, text = "ADDRESS: ")
	addressLabel.grid(row = 7, column = 0, pady = 0)
	addressLabel.config(font = ("Arial", 18))
	address=Entry(root,width=100, borderwidth=5)
	address.grid(row=7, column=1)

	sexLabel = Label(root, text = "SEX: ")
	sexLabel.grid(row = 8, column = 0, pady = 0)
	sexLabel.config(font = ("Arial", 18))
	sex=Entry(root,width=100, borderwidth=5)
	sex.grid(row=8, column=1)

	emailLabel = Label(root, text = "EMAIL: ")
	emailLabel.grid(row = 9, column = 0, pady = 0)
	emailLabel.config(font = ("Arial", 18))
	email=Entry(root,width=100, borderwidth=5)
	email.grid(row=9, column=1)

	phoneLabel = Label(root, text = "PHONE: ")
	phoneLabel.grid(row = 10, column = 0, pady = 0)
	phoneLabel.config(font = ("Arial", 18))
	phone=Entry(root,width=100, borderwidth=5)
	phone.grid(row=10, column=1)

	dobLabel = Label(root, text = "DOB: ")
	dobLabel.grid(row = 11, column = 0, pady = 0)
	dobLabel.config(font = ("Arial", 18))
	dob=Entry(root,width=100, borderwidth=5)
	dob.grid(row=11, column=1)

	cardnoLabel = Label(root, text = "CARD NO.: ")
	cardnoLabel.grid(row = 12, column = 0, pady = 0)
	cardnoLabel.config(font = ("Arial", 18))
	cardno=Entry(root,width=100, borderwidth=5)
	cardno.grid(row=12, column=1)

	cardnameLabel = Label(root, text = "CARD HOLDER NAME: ")
	cardnameLabel.grid(row = 13, column = 0, pady = 0)
	cardnameLabel.config(font = ("Arial", 18))
	cardname=Entry(root,width=100, borderwidth=5)
	cardname.grid(row=13, column=1)

	cvvLabel = Label(root, text = "CVV : ")
	cvvLabel.grid(row = 14, column = 0, pady = 0)
	cvvLabel.config(font = ("Arial", 18))
	cvv=Entry(root,width=100, borderwidth=5)
	cvv.grid(row=14, column=1)

	registerButton = Button(root, text = "REGISTER", command = insert)
	registerButton.grid(row = 15, column = 0, pady = 20, columnspan = 3)
	registerButton.config(font = ("Arial", 18))


	root.mainloop()