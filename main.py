import runpy
from tkinter import *
import sqlite3 as sql
from sqlite3 import Error
from PIL import ImageTk, Image
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

    global account
    global name
    account = cursor.fetchone()
    name = account[0] + " " + account[1]

    if account is not None:
        emailLogin.delete(0, END)
        passwordLogin.delete(0, END)
        for row in account:
            print(row)
        show_frame(homePage)
        Label(homePage, text=f"Hello {name}").grid(row=2, column=2)
    else:
        print("Account information incorrect, please try again")
        errorLabel = Label(root, text="Account information incorrect, please try again")
        errorLabel.grid(row=11, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

def staffLiP():
    show_frame(loginPageStaff)

def staffLogin():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Staff WHERE email=? AND password=?", (staffEmailLogin.get(), staffPasswordLogin.get()))

    global account
    global name
    account = cursor.fetchone()
    name = account[0] + " " + account[1]

    if account is not None:
        emailLogin.delete(0, END)
        passwordLogin.delete(0, END)
        for row in account:
            print(row)
        show_frame(staffPage)
        Label(staffPage, text=f"Hello {name}").grid(row=2, column=2)
    else:
        print("Account information incorrect, please try again")
        errorLabel = Label(root, text="Account information incorrect, please try again")
        errorLabel.grid(row=11, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

def adminLogin():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admins WHERE email=? AND password=?", (adminEmailLogin.get(), adminPasswordLogin.get()))

    global account
    global name
    account = cursor.fetchone()
    name = account[0] + " " + account[1]

    if account is not None:
        emailLogin.delete(0, END)
        passwordLogin.delete(0, END)
        for row in account:
            print(row)
        show_frame(adminPage)
        Label(adminPage, text=f"Hello {name}").grid(row=2, column=2)
    else:
        print("Account information incorrect, please try again")
        errorLabel = Label(root, text="Account information incorrect, please try again")
        errorLabel.grid(row=11, column=2, columnspan=1, pady=5, padx=5, ipadx=0)


def show_frame(frame):
    frame.tkraise()

def test():
    global account
    global name
    account = account
    name = name

#Main program
root = Tk()

#Creating the different pages using frames
loginPage = Frame(root)
homePage = Frame(root)
loginPageStaff = Frame(root)
staffPage = Frame(root)
adminPage = Frame(root)

#adding a grid to each frame
for frame in (loginPage, homePage, loginPageStaff, staffPage, adminPage):
        frame.grid(row=0, column=0, sticky='nsew')

#Shows the login page
show_frame(loginPage)

#Calls functions to set up the database as well as add the default admin account
createDatabase.main()

#creates blank variables for the account as well as the users name
account = []
name = ""

# ------Login page--------
#Entries

entry = Entry(loginPage)

fName = Entry(loginPage, width=30)
fName.grid(row=2, column=2, padx=20)

lName = Entry(loginPage, width=30)
lName.grid(row=3, column=2, padx=20)

email = Entry(loginPage, width=30)
email.grid(row=4, column=2, padx=20)

password = Entry(loginPage, width=30)
password.grid(row=5, column=2, padx=20)

emailLogin = Entry(loginPage, width=30)
emailLogin.grid(row=8, column=2, padx=20)

passwordLogin = Entry(loginPage, width=30)
passwordLogin.grid(row=9, column=2, padx=20)

#Labels
Label(loginPage, text="Register").grid(row=1, column=2)

fNameLabel = Label(loginPage, text="First name")
fNameLabel.grid(row=2, column=1)

lNameLabel = Label(loginPage, text="Last name")
lNameLabel.grid(row=3, column=1)

emailLabel = Label(loginPage, text="Email")
emailLabel.grid(row=4, column=1)

passwordLabel = Label(loginPage, text="Password")
passwordLabel.grid(row=5, column=1)

Label(loginPage, text="Login").grid(row=7, column=2)

emailLabel = Label(loginPage, text="Email")
emailLabel.grid(row=8, column=1)

passwordLabel = Label(loginPage, text="Password")
passwordLabel.grid(row=9, column=1)

#Buttons
submitBtn = Button(loginPage, text="Add user account", command=register)
submitBtn.grid(row=6, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

loginBtn = Button(loginPage, text="Login", command=login)
loginBtn.grid(row=10, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

staffBtn = Button(loginPage, text="Staff login", command=staffLiP)
staffBtn.grid(row=11, column=1, columnspan=1, pady=5, padx=5, ipadx=0)


# ------Home page--------
Label(homePage, text=f"Hello {name}").grid(row=2, column=2)
randomBtn = Button(homePage, text="test", command=test)
randomBtn.grid(row=11, column=1, columnspan=1, pady=5, padx=5, ipadx=0)

# ------Staff login--------
#---Admin Login---
#Entry
adminEmailLogin = Entry(loginPageStaff, width=30)
adminEmailLogin.grid(row=2, column=2, padx=20)

adminPasswordLogin = Entry(loginPageStaff, width=30)
adminPasswordLogin.grid(row=3, column=2, padx=20)

#Label
Label(loginPageStaff, text="Admin login").grid(row=1, column=2)

emailLabel = Label(loginPageStaff, text="Email")
emailLabel.grid(row=2, column=1)

passwordLabel = Label(loginPageStaff, text="Password")
passwordLabel.grid(row=3, column=1)

#Button
loginBtn = Button(loginPageStaff, text="Login", command=adminLogin)
loginBtn.grid(row=4, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

#---Staff login---
staffEmailLogin = Entry(loginPageStaff, width=30)
staffEmailLogin.grid(row=9, column=2, padx=20)

staffPasswordLogin = Entry(loginPageStaff, width=30)
staffPasswordLogin.grid(row=10, column=2, padx=20)

#Label
Label(loginPageStaff, text="Staff login").grid(row=8, column=2)
Label(loginPageStaff, text="").grid(row=5, column=2)

emailLabel = Label(loginPageStaff, text="Email")
emailLabel.grid(row=9, column=1)

passwordLabel = Label(loginPageStaff, text="Password")
passwordLabel.grid(row=10, column=1)

#Button
loginBtn = Button(loginPageStaff, text="Login", command=staffLogin)
loginBtn.grid(row=11, column=2, columnspan=1, pady=5, padx=5, ipadx=0)

# ------Staff home page--------
Label(staffPage, text=f"Hello {name}").grid(row=2, column=2)
randomBtn = Button(staffPage, text="test", command=test)
randomBtn.grid(row=11, column=1, columnspan=1, pady=5, padx=5, ipadx=0)

# ------Admin home page--------
Label(adminPage, text=f"Hello {name}").grid(row=2, column=2)
randomBtn = Button(adminPage, text="test", command=test)
randomBtn.grid(row=11, column=1, columnspan=1, pady=5, padx=5, ipadx=0)


root.mainloop()
