import sqlite3
from tkinter import messagebox
from tkinter import *
import os
import re

window = Tk()


def back():
    window.destroy()
    # import std_login
    os.system('std_login.py')


name_var = StringVar()
reg_var = StringVar()
pwd_var = StringVar()

f1 = Frame(window)
f1.place(x=190, y=20)

title = Label(f1, text="Student Sign Up", font=("Time Roman", 35, "bold"), bg="white", padx=10, pady=10, relief=RIDGE,
              bd=10)
title.pack(fill="both")

f2 = Frame(window, width=350, height=200, bg="#fff5b8")
f2.place(x=220, y=140)

nameL = Label(f2, text='Student name ', padx=5, pady=5, font=('Verdana', 10, "bold"), bg="#fff5b8", fg="black")
nameL.place(x=10, y=10)

nameE = Entry(f2, textvariable=name_var, width=25)
nameE.place(x=150, y=14)

regL = Label(f2, text='Student Id', padx=5, pady=5, font=('Verdana', 10, "bold"), bg="#fff5b8", fg="black")
regL.place(x=10, y=60)

regE = Entry(f2, textvariable=reg_var, width=25)
regE.place(x=150, y=64)

pwdL = Label(f2, text='Password', padx=5, pady=5, font=('Verdana', 10, "bold"), bg="#fff5b8", fg="black")
pwdL.place(x=10, y=110)

pwdE = Entry(f2, textvariable=pwd_var, show="*", width=25)
pwdE.place(x=150, y=114)


def cancel():
    window.destroy()
    # import common
    os.system('common.py')


def reset():
    name_var.set("")
    reg_var.set("")
    pwd_var.set("")


def is_strong_password(password):
    # Check if password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False
    # Check if password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False
    # Check if password contains at least one digit
    if not re.search(r"\d", password):
        return False
    # Check if password contains at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False
    return True


def submit():
    try:
        password = pwd_var.get()
        if not is_strong_password(password):
            messagebox.showerror("Weak Password",
                                 "Password must contain at least one uppercase letter, one lowercase letter, one digit, one special character, and have a minimum length of 8 characters.")
            return

        con = sqlite3.connect('registration_student.db')
        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS student_signUP (name TEXT, student_id TEXT, password TEXT)")

        cur.execute("INSERT INTO student_signUP VALUES (?, ?, ?)", (name_var.get(), reg_var.get(), pwd_var.get()))

        con.commit()
        con.close()

        messagebox.showinfo("", "Registered successfully")

        # import std_login
        os.system('std_login.py')

        reset()

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


button_frame = Frame(window, bg='#fff5b8', height=100, width=400, padx=20)
button_frame.place(x=250, y=350)

sub_b1 = Button(button_frame, text='Submit', font='Verdana 10 bold', command=submit)
sub_b1.place(x=10, y=10)

can_b1 = Button(button_frame, text='Cancel', font='Verdana 10 bold', command=cancel)
can_b1.place(x=90, y=10)

reset_b1 = Button(button_frame, text='Reset', font='Verdana 10 bold', command=reset)
reset_b1.place(x=170, y=10)
#
# back = Button(button_frame, text='Back', padx=10, pady=10, command=back)
# back.place(x=90, y=30)
window.title("sign in")
window.geometry("800x450")
window.config(bg="#fff5b8")
window.mainloop()
