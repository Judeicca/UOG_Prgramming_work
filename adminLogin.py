import sys
from tkinter import *
import sqlite3 as sql
from sqlite3 import Error
from PIL import ImageTk, Image

def adminLogin():
    root = Tk()
    #root.iconbitmap('cat.ico')
    root.title('Home Page')
    # connect to database
    conn = sql.connect("database.db")
    # create cursor
    cursor = conn.cursor()

    Label(root, text="Hello there").pack()

    frame = Frame(root).pack()

    img = ImageTk.PhotoImage(Image.open("rock.jpg"))

    label = Label(frame, image=img).pack()

    root.mainloop()