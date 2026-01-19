from tkinter import *
import sqlite3
from tkinter import messagebox
import os
import re

window = Tk()

name_var = StringVar()
reg_var = StringVar()
pwd_var = StringVar()

f1 = Frame(window)
f1.place(x=180, y=20)

title = Label(
    f1, text="Company Sign Up", font=("Time Roman", 35, "bold"),
    bg="white", padx=10, pady=10, relief=RIDGE, bd=10
)
title.pack(fill="both")

f2 = Frame(window, width=350, height=200, bg="#ffb16e")
f2.place(x=220, y=140)

Label(f2, text='Company name ', font=('Arial', 12, "bold"),
      bg="#ffb16e", fg="white").place(x=10, y=10)
Entry(f2, textvariable=name_var, width=25).place(x=150, y=14)

Label(f2, text='Company Id', font=('Arial', 12, "bold"),
      bg="#ffb16e", fg="white").place(x=10, y=60)
Entry(f2, textvariable=reg_var, width=25).place(x=150, y=64)

Label(f2, text='Password', font=('Arial', 12, "bold"),
      bg="#ffb16e", fg="white").place(x=10, y=110)
Entry(f2, textvariable=pwd_var, show="*", width=25).place(x=150, y=114)


def is_strong_password(password):
    if not re.search(r"[A-Z]", password): return False
    if not re.search(r"[a-z]", password): return False
    if not re.search(r"\d", password): return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): return False
    if len(password) < 8: return False
    return True


def submit():
    if not is_strong_password(pwd_var.get()):
        messagebox.showerror("Weak Password", "Password not strong enough")
        return

    conn = sqlite3.connect('registration_student.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS company_login (
            name TEXT,
            id TEXT PRIMARY KEY,
            password TEXT
        )
    ''')

    cur.execute(
        "INSERT INTO company_login VALUES (?, ?, ?)",
        (name_var.get(), reg_var.get(), pwd_var.get())
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("", "Registered successfully")
    window.destroy()
    os.system('cmp_login.py')


def cancel():
    window.destroy()
    os.system('common.py')


def reset():
    name_var.set("")
    reg_var.set("")
    pwd_var.set("")


button_frame = Frame(window, bg='#fff5b8', height=100, width=400)
button_frame.place(x=250, y=350)

Button(button_frame, text='Submit', command=submit).place(x=10, y=10)
Button(button_frame, text='Cancel', command=cancel).place(x=90, y=10)
Button(button_frame, text='Reset', command=reset).place(x=170, y=10)

window.geometry("800x450")
window.config(bg="#fff5b8")
window.mainloop()
