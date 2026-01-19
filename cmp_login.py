import sqlite3
from tkinter import messagebox
import tkinter as tk
import os

win = tk.Tk()

def cancel():
    win.destroy()
    os.system('common.py')

def clear():
    userentry.delete(0, tk.END)
    passentry.delete(0, tk.END)

def login():
    if user_id.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter Company ID And Password")
    else:
        try:
            conn = sqlite3.connect('registration_student.db')
            cur = conn.cursor()

            cur.execute(
                "SELECT * FROM company_login WHERE id=? AND password=?",
                (user_id.get(), password.get())
            )

            row = cur.fetchone()

            if row:
                messagebox.showinfo("Success", "Successfully Login")
                win.destroy()
                os.system('cmp.py')
            else:
                messagebox.showerror("Error", "Invalid Company ID Or Password")

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}")


def signup():
    win.destroy()
    os.system('cmp_signup.py')


win.title("Company login")
win.maxsize(width=500, height=500)
win.minsize(width=500, height=500)

heading = tk.Label(win, text="Company Login", font='Verdana 20 bold',
                   bg='#fff5b8', fg='black')
heading.place(x=80, y=150)

tk.Label(win, text="User ID :", bg='#fff5b8', font='Verdana 10',
         fg='black').place(x=80, y=220)
tk.Label(win, text="Password :", bg='#fff5b8', font='Verdana 10',
         fg='black').place(x=80, y=260)

user_id = tk.StringVar()
password = tk.StringVar()

userentry = tk.Entry(win, width=40, textvariable=user_id)
userentry.place(x=200, y=223)

passentry = tk.Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

tk.Button(win, text="Login", command=login).place(x=150, y=293)
tk.Button(win, text="Clear", command=clear).place(x=210, y=293)
tk.Button(win, text="SignUp", command=signup).place(x=270, y=293)
tk.Button(win, text="Home", command=cancel).place(x=340, y=293)

win.config(bg="#fff5b8")
win.mainloop()
