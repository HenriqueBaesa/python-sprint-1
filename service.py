
import hashlib
from tkinter import *
import sqlite3
from helpers import validate_cpf


conn = sqlite3.connect('porto.db')
c = conn.cursor()


def register_user(email, cpf, password):
    # check if email is valid
    if not email or "@" not in email or "." not in email:
        print("Invalid email")
        return

    # check if cpf is valid
    if not cpf or validate_cpf(cpf) is False:
        print("Invalid cpf")
        return

    # check if password is valid
    if not password or len(password) < 6:
        print("Invalid password")
        return
    
    # using SHA-256 to hash the password
    password = hashlib.sha256(password.encode()).hexdigest()

    # register user to database
    c.execute("INSERT INTO users (email, cpf, password) VALUES (?, ?, ?)", (email, cpf, password))
    conn.commit()

    # tkinter pop up message
    root = Tk()
    root.title("Success")
    root.geometry("300x300")
    label = Label(root, text="User registered successfully")
    label.pack()
    root.mainloop()


def login_user(email, password):
    # check if email is valid
    if not email or "@" not in email or "." not in email:
        print("Invalid email")
        return

    # check if password is valid
    if not password or len(password) < 6:
        print("Invalid password")
        return
    
    # get the hashed password
    password = hashlib.sha256(password.encode()).hexdigest()

    # check if user exists in database
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()

    if user:
        # tkinter pop up message
        root = Tk()
        root.title("Success")
        root.geometry("300x300")
        label = Label(root, text="User logged in successfully")
        label.pack()
        root.mainloop()
    else:
        print("Invalid email or password")


def add_car(car_type, car_brand, car_model, car_year, car_version):
    # check if car_type is valid
    if not car_type:
        print("Invalid car type")
        return

    # check if car_brand is valid
    if not car_brand:
        print("Invalid car brand")
        return

    # check if car_model is valid
    if not car_model:
        print("Invalid car model")
        return

    # check if car_year is valid
    if not car_year or not car_year.isdigit() or len(car_year) != 4:
        print("Invalid car year")
        return

    # check if car_version is valid
    if not car_version:
        print("Invalid car version")
        return

    # register car to database
    c.execute("INSERT INTO cars (car_type, car_brand, car_model, car_year, car_version) VALUES (?, ?, ?, ?, ?)", (car_type, car_brand, car_model, car_year, car_version))
    conn.commit()

    # tkinter pop up message
    root = Tk()
    root.title("Success")
    root.geometry("300x300")
    label = Label(root, text="Car added successfully")
    label.pack()
    root.mainloop()

def view_car():
    # get all cars from database
    c.execute("SELECT * FROM cars")
    cars = c.fetchall()

    # tkinter pop up message
    root = Tk()
    root.title("Cars")
    root.geometry("300x300")
    label = Label(root, text=cars)
    label.pack()
    root.mainloop()

def delete_car(car_id):
    # check if car_id is valid
    if not car_id or not car_id.isdigit():
        print("Invalid car id")
        return

    # delete car from database
    c.execute("DELETE FROM cars WHERE id = ?", (car_id,))
    conn.commit()

    # tkinter pop up message
    root = Tk()
    root.title("Success")
    root.geometry("300x300")
    label = Label(root, text="Car deleted successfully")
    label.pack()
    root.mainloop()