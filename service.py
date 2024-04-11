
from tkinter import *
import sqlite3
from helpers import validate_cpf


conn = sqlite3.connect('car_rental.db')
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