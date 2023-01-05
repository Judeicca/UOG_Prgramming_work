import runpy
from tkinter import *
import sqlite3 as sql
from sqlite3 import Error
import loginPage
import createDatabase


def register():

    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()
    #insert into table
    try:
        cursor.execute("INSERT INTO Users VALUES (:first_name, :last_name, :email, :password)",
                    {
                        'first_name':fName.get(),
                        'last_name':lName.get(),
                        'email':email.get(),
                        'password':password.get()
                    })
        fName.delete(0, END)
        lName.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)
    except Error as e:
        print("Account already exists")
        fName.delete(0, END)
        lName.delete(0, END)
        email.delete(0, END)
        password.delete(0, END)

    cursor.execute("SELECT rowid, * FROM users")
    items = cursor.fetchall()

    for item in items:
        print(item)

        conn.commit()

def login():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE email=? AND password=?", (emailLogin.get(), passwordLogin.get()))

    account = cursor.fetchone()

    if account is not None:
        emailLogin.delete(0, END)
        passwordLogin.delete(0, END)
        for row in account:
            print(row)
        root.destroy()
        loginPage.homePage()
    else:
        print("Error")


def createAdmin():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Admins (first_name, last_name, email, password) VALUES ('Admin', '', 'admin@org.com', '@Password123')")
    except Error:
        pass
    conn.commit()

#Main program
root = Tk()
root.title('Register a user account')
#root.iconbitmap('cat.ico')
entry = Entry(root)

createDatabase.main()
createAdmin()

#Entries
fName = Entry(root, width=30)
fName.grid(row=2, column=2, padx=20)

lName = Entry(root, width=30)
lName.grid(row=3, column=2, padx=20)

email = Entry(root, width=30)
email.grid(row=4, column=2, padx=20)

password = Entry(root, width=30)
password.grid(row=5, column=2, padx=20)

emailLogin = Entry(root, width=30)
emailLogin.grid(row=8, column=2, padx=20)

passwordLogin = Entry(root, width=30)
passwordLogin.grid(row=9, column=2, padx=20)

#Labels
Label(root, text="Register").grid(row=1, column=2)

fNameLabel = Label(root, text="First name")
fNameLabel.grid(row=2, column=1)

lNameLabel = Label(root, text="Last name")
lNameLabel.grid(row=3, column=1)

emailLabel = Label(root, text="Email")
emailLabel.grid(row=4, column=1)

passwordLabel = Label(root, text="Password")
passwordLabel.grid(row=5, column=1)

Label(root, text="Login").grid(row=7, column=2)

emailLabel = Label(root, text="Email")
emailLabel.grid(row=8, column=1)

passwordLabel = Label(root, text="Password")
passwordLabel.grid(row=9, column=1)

#Buttons
submitBtn = Button(root, text="Add user account", command=register)
submitBtn.grid(row=6, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

loginBtn = Button(root, text="Login", command=login)
loginBtn.grid(row=10, column=2, columnspan=1, pady=5, padx=5, ipadx=0)


root.mainloop()
