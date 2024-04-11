from tkinter import *
from validate_docbr import CPF
import sqlite3

from service import *


# sqlite database connection
conn = sqlite3.connect('car_rental.db')
c = conn.cursor()

# create user table with autoincrement id
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()



# tkinter button menu with register, login, add car, view car, delete car, and exit buttons
def menu():
    root = Tk()
    root.title("Car Rental System")
    root.geometry("300x300")

    # register button
    register_button = Button(root, text="Register", command=register)
    register_button.pack()

    # login button
    login_button = Button(root, text="Login", command=login)
    login_button.pack()

    # add car button
    add_car_button = Button(root, text="Add Car", command=add_car)
    add_car_button.pack()

    # view car button
    view_car_button = Button(root, text="View Car", command=view_car)
    view_car_button.pack()

    # delete car button
    delete_car_button = Button(root, text="Delete Car", command=delete_car)
    delete_car_button.pack()

    # exit button
    exit_button = Button(root, text="Exit", command=root.quit)
    exit_button.pack()

    root.mainloop()


# register user with email, cpf and password. Validate if user input is valid
def register():
    root = Tk()
    root.title("Register")
    root.geometry("300x300")

    # email label and entry
    email_label = Label(root, text="Email")
    email_label.pack()
    email_entry = Entry(root)
    email_entry.pack()

    # cpf label and entry
    cpf_label = Label(root, text="CPF")
    cpf_label.pack()
    cpf_entry = Entry(root)
    cpf_entry.pack()

    # password label and entry
    password_label = Label(root, text="Password")
    password_label.pack()
    password_entry = Entry(root)
    password_entry.pack()

    # register button + validating input + registering user
    register_button = Button(root, text="Register", command=lambda: register_user(email_entry.get(), cpf_entry.get(), password_entry.get()))
    register_button.pack()

    root.mainloop()
    return



def login():
    root = Tk()
    root.title("Login")
    root.geometry("300x300")

    # email label and entry
    email_label = Label(root, text="Email")
    email_label.pack()
    email_entry = Entry(root)
    email_entry.pack()

    # password label and entry
    password_label = Label(root, text="Password")
    password_label.pack()
    password_entry = Entry(root)
    password_entry.pack()

    # login button
    login_button = Button(root, text="Login", command=lambda: login_user(email_entry.get(), password_entry.get()))
    login_button.pack()

    root.mainloop()
    return




def add_car():
    return

def view_car():
    return

def delete_car():
    return

menu()