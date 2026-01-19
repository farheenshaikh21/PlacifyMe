import sqlite3
from tkinter import messagebox
import tkinter as tk
import os

win = tk.Tk()


def clear():
    userentry.delete(0, tk.END)
    passentry.delete(0, tk.END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        try:
            conn = sqlite3.connect('registration_student.db')
            cur = conn.cursor()

            cur.execute("SELECT * FROM admin WHERE user_name=? AND Password=?", (user_name.get(), password.get()))
            row = cur.fetchall()

            if not row:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=win)
            else:
                messagebox.showinfo("Success", "Login Successful!")

                # import selected
                os.system('selected.py')

                close()

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=win)


win.title("login")

win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

heading = tk.Label(win, text="Admin Login", font='Verdana 20 bold', bg='#fff5b8', fg='black')
heading.place(x=130, y=150)

username = tk.Label(win, text="User Name :", font='Verdana 10', bg="#fff5b8", fg='black')
username.place(x=80, y=220)

userpass = tk.Label(win, text="Password :", font='Verdana 10', bg="#fff5b8", fg='black')
userpass.place(x=80, y=260)

user_name = tk.StringVar()
password = tk.StringVar()

userentry = tk.Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = tk.Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

btn_login = tk.Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)

btn_clr = tk.Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_clr.place(x=260, y=293)

win.config(bg="#fff5b8")

win.mainloop()
