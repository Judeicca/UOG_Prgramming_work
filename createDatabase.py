from tkinter import *
import sqlite3 as sql
from sqlite3 import Error
import loginPage


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

        # create stock table
        create_table(conn,sql_create_stock_table)
    else:
        print("Error! cannot create the database connection.")