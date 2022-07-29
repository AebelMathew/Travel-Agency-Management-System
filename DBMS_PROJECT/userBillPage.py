from tkinter import *
import pymysql
from userFinalPaySuccess import *
from userFinalPayFail import *

def displayBill(name, customerID, CityID, HotelID, NumOfRooms, TransportProvider, TypeOfTransport, NumOfSeats):
	root = Tk()
	connection = pymysql.connect(host = "localhost", user = "root", passwd = "shaurya3027#", database = "test")
	cursor = connection.cursor()

	def payBill(creditCardNumber, cvv):
		detailsCorrect = False
		retrieve = "Select Card_No, CVV from card_info where Customer_ID = %s;"
		data = (customerID)
		cursor.execute(retrieve,data)
		cardDetails = cursor.fetchall()
		if(creditCardNumber == int(cardDetails[0][0])):
			if(cvv == int(cardDetails[0][1])):
				detailsCorrect = True
		connection.commit()
		connection.close()
		root.destroy()
		if(detailsCorrect):
			displayFinalSuccess()
		else:
			displayFinalFail()

	projectName = Label(root, text = "Travel Agency Management System")
	projectName.grid(row = 0, column = 0, pady = 10, columnspan = 3)
	projectName.config(width = 50)
	projectName.config(font = ("Arial", 24))

	windowHeading = Label(root, text = "Invoice")
	windowHeading.grid(row = 1, column = 0, pady = 10, columnspan = 3)
	windowHeading.config(font = ("Arial", 22))

	customerNameLabel = Label(root, text = "Customer Name : " + name)
	customerNameLabel.grid(row = 2, column = 0, pady = 10, columnspan = 3)
	customerNameLabel.config(font = ("Arial", 16))

	retrieve = "Select Card_Holder_Name from card_info where Customer_ID = %s;"
	data = (customerID)
	cursor.execute(retrieve,data)
	nameOnBill = cursor.fetchall()
	connection.commit()

	billNameLabel = Label(root, text = "Name on Bill : " + nameOnBill[0][0])
	billNameLabel.grid(row = 3, column = 0, pady = 10, columnspan = 3)
	billNameLabel.config(font = ("Arial", 16))

	retrieve2 = "Select City_Name from cities where City_ID = %s;"
	data2 = (CityID)
	cursor.execute(retrieve2,data2)
	cityName = cursor.fetchall()
	connection.commit()

	cityNameLabel = Label(root, text = "City Name : " + cityName[0][0])
	cityNameLabel.grid(row = 4, column = 0, pady = 10, columnspan = 3)
	cityNameLabel.config(font = ("Arial", 16))

	retrieve3 = "Select Hotel_Name, Price from hotels where Hotel_ID = %s;"
	data3 = (HotelID)
	cursor.execute(retrieve3,data3)
	hotelName = cursor.fetchall()
	connection.commit()

	hotelNameLabel = Label(root, text = "Hotel Name : " + hotelName[0][0])
	hotelNameLabel.grid(row = 5, column = 0, pady = 10, columnspan = 3)
	hotelNameLabel.config(font = ("Arial", 16))

	transportProviderLabel = Label(root, text = "Transport : " + TransportProvider)
	transportProviderLabel.grid(row = 6, column = 0, pady = 10, columnspan = 3)
	transportProviderLabel.config(font = ("Arial", 16))

	totalPrice = (int(hotelName[0][1]) * NumOfRooms)

	retrieve4 = "Select Cost from train where Provider = %s;"
	retrieve5 = "Select Cost from bus where Provider = %s;"
	retrieve6 = "Select Cost from airplane where Provider = %s;"
	data4 = (TransportProvider)

	if(TypeOfTransport == "TRAIN"):
		cursor.execute(retrieve4,data4)
		price1 = cursor.fetchall()
	elif(TypeOfTransport == "BUS"):
		cursor.execute(retrieve5,data4)
		price1 = cursor.fetchall()
	elif(TypeOfTransport == "AIRPLANE"):
		cursor.execute(retrieve6,data4)
		price1 = cursor.fetchall()
	connection.commit()
	totalPrice += (int(price1[0][0]) * NumOfSeats)

	BillLabel = Label(root, text = "Total Cost : " + str(totalPrice))
	BillLabel.grid(row = 7, column = 0, pady = 10, columnspan = 3)
	BillLabel.config(font = ("Arial", 16))

	creditCardNumberLabel = Label(root, text = "Enter your Credit Card Number : ")
	creditCardNumberLabel.grid(row = 8, column = 0, pady = 10, columnspan = 3)
	creditCardNumberLabel.config(font = ("Arial", 16))
	creditCardNumber = Entry(root, width=50, borderwidth=5)
	creditCardNumber.grid(row=9, column=0, columnspan = 3)

	cvvLabel = Label(root, text = "Enter your CVV : ")
	cvvLabel.grid(row = 10, column = 0, pady = 10, columnspan = 3)
	cvvLabel.config(font = ("Arial", 16))
	cvv = Entry(root, width=50, borderwidth=5)
	cvv.grid(row=11, column=0, columnspan = 3)

	payButton = Button(root, text = "PAY", command = lambda : payBill(int(creditCardNumber.get()), int(cvv.get())))
	payButton.grid(row = 101, column = 0, pady = 20, columnspan = 6)
	payButton.config(font = ("Arial", 18))