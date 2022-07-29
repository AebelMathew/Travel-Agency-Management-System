from tkinter import *
from userRegisterPage import *
from LoginPage import *
root = Tk()

projectName = Label(root, text = "Travel Agency Management System")
projectName.grid(row = 0, column = 1, pady = 10, columnspan = 3)
projectName.config(width = 50)
projectName.config(font = ("Arial", 24))

windowHeading = Label(root, text = "MAIN PAGE")
windowHeading.grid(row = 1, column = 1, pady = 10, columnspan = 3)
windowHeading.config(font = ("Arial", 22))

loginButton = Button(root, text = "Login", command = displayLoginPage)
loginButton.grid(row = 5, column = 0, pady = 10, columnspan = 3)
loginButton.config(font = ("Arial", 18))

registerButton = Button(root, text = "Register", command = displayRegistration)
registerButton.grid(row = 5, column = 2, pady = 10, columnspan = 3)
registerButton.config(font = ("Arial", 18))

quitButton = Button(root, text = "Quit!", command = root.destroy)
quitButton.grid(row = 6, column = 1, pady = 20, columnspan = 3)
quitButton.config(font = ("Arial", 18))

root.mainloop()