from tkinter import *
from validate_docbr import CPF
import sqlite3

import service as car_service


# sqlite database connection
conn = sqlite3.connect('porto.db')
c = conn.cursor()

# create user table with autoincrement id
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL,
    password TEXT NOT NULL
)''')

# create car table with autoincrement id
c.execute('''CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_type TEXT NOT NULL,
    car_brand TEXT NOT NULL,
    car_model TEXT NOT NULL,
    car_year TEXT NOT NULL,
    car_version TEXT NOT NULL
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
    register_button = Button(root, text="Register", command=lambda: car_service.register_user(email_entry.get(), cpf_entry.get(), password_entry.get()))
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
    login_button = Button(root, text="Login", command=lambda: car_service.login_user(email_entry.get(), password_entry.get()))
    login_button.pack()

    root.mainloop()
    return



# fileds: car_type, car_brand, car_model, car_year, car_version
def add_car():
    root = Tk()
    root.title("Add Car")
    root.geometry("300x300")

    # car type label and entry
    car_type_label = Label(root, text="Car Type")
    car_type_label.pack()
    car_type_entry = Entry(root)
    car_type_entry.pack()

    # car brand label and entry
    car_brand_label = Label(root, text="Car Brand")
    car_brand_label.pack()
    car_brand_entry = Entry(root)
    car_brand_entry.pack()

    # car model label and entry
    car_model_label = Label(root, text="Car Model")
    car_model_label.pack()
    car_model_entry = Entry(root)
    car_model_entry.pack()

    # car year label and entry
    car_year_label = Label(root, text="Car Year")
    car_year_label.pack()
    car_year_entry = Entry(root)
    car_year_entry.pack()

    # car version label and entry
    car_version_label = Label(root, text="Car Version")
    car_version_label.pack()
    car_version_entry = Entry(root)
    car_version_entry.pack()

    # add car button
    add_car_button = Button(root, text="Add Car", command=lambda: car_service.add_car(car_type_entry.get(), car_brand_entry.get(), car_model_entry.get(), car_year_entry.get(), car_version_entry.get()))
    add_car_button.pack()

    root.mainloop()
    return


def view_car():
    root = Tk()
    root.title("View Car")
    root.geometry("300x300")

    # view car button
    view_car_button = Button(root, text="View Car", command=car_service.view_car)
    view_car_button.pack()

    root.mainloop()
    return


def delete_car():
    root = Tk()
    root.title("Delete Car")
    root.geometry("300x300")

    # car id label and entry
    car_id_label = Label(root, text="Car ID")
    car_id_label.pack()
    car_id_entry = Entry(root)
    car_id_entry.pack()

    # delete car button
    delete_car_button = Button(root, text="Delete Car", command=lambda: car_service.delete_car(car_id_entry.get()))
    delete_car_button.pack()

    root.mainloop()
    return

menu()