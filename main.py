import os
from tkinter import *
import sqlite3 as sql
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sql.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "database.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS Users (
                                        first_name text CHAR(20) NOT NULL,
                                        last_name text CHAR(20) NOT NULL,
                                        email text CHAR(20) NOT NULL,
                                        password text CHAR(20) NOT NULL,
                                        PRIMARY KEY (email)
                                    ); """

    sql_create_admins_table = """CREATE TABLE IF NOT EXISTS Admins (
                                        first_name text NOT NULL,
                                        last_name text,
                                        email text,
                                        password text
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)

        # create tasks table
        create_table(conn, sql_create_admins_table)
    else:
        print("Error! cannot create the database connection.")

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
        for row in account:
            print(row)
    else:
        print("Email or password are incorrect")


#Main program
root = Tk()
root.title('Register a user account')
root.iconbitmap('cat.ico')
entry = Entry(root)

main()

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
