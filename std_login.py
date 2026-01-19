import sqlite3
from tkinter import messagebox
from tkinter import *
import os

win = Tk()

def cancel():
    win.destroy()
    #import common
    os.system('common.py')

def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)

def close():
    win.destroy()

def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User ID And Password", parent=win)
    else:
        try:
            con = sqlite3.connect('registration_student.db')
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM student_signUP WHERE student_id=? AND password=?",
                (user_name.get().strip(), password.get().strip())
            )

            row = cur.fetchone()

            if row:
                messagebox.showinfo("Success", "Successfully Login")
                win.destroy()
                os.system('student.py')
            else:
                messagebox.showerror("Error", "Invalid User ID Or Password")

            con.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}")

def signup():
    win.destroy()
    # import std_signup
    os.system('std_signup.py')

win.title("Login")

win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

heading = Label(win, text="Student Login", font='Verdana 20 bold', bg='#fff5b8', fg='black')
heading.place(x=120, y=150)

username = Label(win, text="User ID :", font='Verdana 10 bold', bg="#fff5b8", fg='black')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 10 bold', bg="#fff5b8", fg='black')
userpass.place(x=80, y=260)

user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=150, y=293)

btn_clear = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_clear.place(x=210, y=293)

btn_sign = Button(win, text="SignUp", font='Verdana 10 bold', command=signup)
btn_sign.place(x=270, y=293)

btn_home = Button(win, text="Home", font='Verdana 10 bold', command=cancel)
btn_home.place(x=340, y=293)

win.config(bg="#fff5b8")

win.mainloop()
