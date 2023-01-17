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

def createStaff():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    #Try to add a default staff account into the staff table, however if an error arrises then this statement will be passed
    try:
        cursor.execute("INSERT INTO Staff (first_name, last_name, email, password) VALUES ('S', 'Taff', 'S', 'S')")
    except Error:
        pass
    #Commit the changes to the database
    conn.commit()

def createAdmin():
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    #Try to add a default admin account into the admins table, however if an error arrises then this statement will be passed
    try:
        cursor.execute("INSERT INTO Admins (first_name, last_name, email, password) VALUES ('Admin', '', 'admin@org.com', '@Password123')")
    except Error:
        pass
    #Commit the changes to the database
    conn.commit()

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
                                        first_name text CHAR(20) NOT NULL,
                                        last_name text CHAR(20),
                                        email text CHAR(20),
                                        password text CHAR(20),
                                        PRIMARY KEY (email)
                                );"""

    sql_create_staff_table = """CREATE TABLE IF NOT EXISTS Staff (
                                        first_name text CHAR(20) NOT NULL,
                                        last_name text CHAR(20),
                                        email text CHAR(20),
                                        password text CHAR(20),
                                        PRIMARY KEY (email)
                                );"""

    sql_create_stock_table = """CREATE TABLE IF NOT EXISTS Stock (
                                        stockID PRIMARY KEY
                                        name text,
                                        qty,
                                        qty left
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_users_table)

        # create tasks table
        create_table(conn, sql_create_admins_table)

        #create staff table
        create_table(conn, sql_create_staff_table)

        # create stock table
        create_table(conn,sql_create_stock_table)
    else:
        print("Error! cannot create the database connection.")

    createAdmin()
    createStaff()