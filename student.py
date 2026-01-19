from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os

window = Tk()

name_var = StringVar()
reg_var = StringVar()
bran_var = StringVar()
cgpa_var = StringVar()
year_var = StringVar()
phone_var = StringVar()
gender_var = StringVar()
email_var = StringVar()
search_var = StringVar()
del_var = StringVar()
cet_var = StringVar()
company_var = StringVar()

f1 = Frame(window)
f1.place(x=330, y=20)

title = Label(f1, text="Student Registration", font=("Time Roman", 45, "bold"), bg="white", padx=10, pady=10,
              relief=RIDGE, bd=10)
title.pack(fill="both")

f2 = Frame(window, width=350, height=500, bg="#ffb16e")
f2.place(x=30, y=140)

nameL = Label(f2, text='Full name ', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
nameL.place(x=10, y=10)

nameE = Entry(f2, textvariable=name_var, width=25)
nameE.place(x=150, y=14)

emailL = Label(f2, text='Email id', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
emailL.place(x=10, y=60)

emailE = Entry(f2, textvariable=email_var, width=25)
emailE.place(x=150, y=64)

phoneL = Label(f2, text='Phone no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
phoneL.place(x=10, y=110)

phoneE = Entry(f2, textvariable=phone_var, width=25)
phoneE.place(x=150, y=114)

genderL = Label(f2, text='Gender', font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
genderL.place(x=10, y=160)

genderE = ttk.Combobox(f2, textvariable=gender_var, width=22)
genderE['values'] = ("Female", "Male", "Other")
genderE.place(x=150, y=164)

regL = Label(f2, text='Registration no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
regL.place(x=10, y=210)

regE = Entry(f2, textvariable=reg_var, width=25)
regE.place(x=150, y=214)

branchL = Label(f2, text='Branch', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
branchL.place(x=10, y=260)

branchE = Entry(f2, textvariable=bran_var, width=25)
branchE.place(x=150, y=264)

yearL = Label(f2, text='Year', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
yearL.place(x=10, y=310)

yearE = ttk.Combobox(f2, textvariable=year_var, width=22)
yearE['values'] = ("TE", "BE")
yearE.place(x=150, y=314)

cgpaL = Label(f2, text='CGPA', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
cgpaL.place(x=10, y=360)

cgpaE = Entry(f2, textvariable=cgpa_var, width=25)
cgpaE.place(x=150, y=364)

cetL = Label(f2, text='CET/JEE', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
cetL.place(x=10, y=410)

cetE = Entry(f2, textvariable=cet_var, width=25)
cetE.place(x=150, y=414)

companyL = Label(f2, text='Company Name', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
companyL.place(x=10, y=460)

companyE = Entry(f2, textvariable=company_var, width=25)
companyE.place(x=150, y=464)


def next():
    window.destroy()


def DisplayData():
    for i in student_table.get_children():
        student_table.delete(i)
    conn = sqlite3.connect('registration_student.db', timeout=10)
    cur = conn.cursor()
    cur.execute("SELECT * FROM student_table")
    result = cur.fetchall()
    if len(result) != 0:
        for row in result:
            student_table.insert('', END, values=row)
    conn.commit()
    conn.close()


def submit():
    try:
        conn = sqlite3.connect('registration_student.db', timeout=10)
        cur = conn.cursor()
        cur.execute("INSERT INTO student_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (name_var.get(), email_var.get(), phone_var.get(), gender_var.get(), reg_var.get(), bran_var.get(),
                     year_var.get(), cgpa_var.get(), cet_var.get(), company_var.get()))
        conn.commit()
        conn.close()
        DisplayData()
        messagebox.showinfo("", "Data Added successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")




def cancel():
    window.destroy()


def search():
    conn = sqlite3.connect('registration_student.db', timeout=10)
    cur = conn.cursor()
    cur.execute("SELECT * FROM student_table WHERE Registration_no=?", (search_var.get(),))
    result = cur.fetchone()
    if result:
        name_var.set(result[0])
        email_var.set(result[1])
        phone_var.set(result[2])

        gender_var.set(result[3])
        reg_var.set(result[4])
        bran_var.set(result[5])
        year_var.set(result[6])
        cgpa_var.set(result[7])
        cet_var.set(result[8])
        company_var.set(result[9])
        student_table.delete(*student_table.get_children())
        student_table.insert('', END, values=result)
    else:
        messagebox.showerror("Error", "No record found")
    conn.close()


def delete():
    conn = sqlite3.connect('registration_student.db', timeout=10)
    cur = conn.cursor()
    cur.execute("DELETE FROM student_table WHERE Registration_no=?", (reg_var.get(),))
    conn.commit()
    conn.close()
    DisplayData()
    messagebox.showinfo("Record deleted", reg_var.get() + " this record is deleted successfully")


def reset():
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    gender_var.set("")
    reg_var.set("")
    bran_var.set("")
    year_var.set("")
    cgpa_var.set("")
    cet_var.set("")
    company_var.set("")


def view_upcoming_companies():
    os.system('cmp_up.py')


sub_b1 = Button(text='Submit', font='Verdana 10 bold', command=submit)
sub_b1.place(x=105, y=650)



dlt_b1 = Button(text='Delete', font='Verdana 10 bold', command=delete)
dlt_b1.place(x=180, y=650)

reset_b1 = Button(text='Reset', font='Verdana 10 bold', command=reset)
reset_b1.place(x=250, y=650)

home_b1 = Button(text='Home', font='Verdana 10 bold', command=cancel)
home_b1.place(x=315, y=650)

upcoming_b1 = Button(text='Upcoming Companies', font='Verdana 10 bold', command=view_upcoming_companies)
upcoming_b1.place(x=400, y=650)

frame11 = Frame(window, width=900, height=500, bg="#ffb16e")
frame11.place(x=400, y=140)

next_b1 = Button(text='NEXT >>', font='Verdana 10 bold', command=next)
next_b1.place(x=1100, y=650)

search_frame = Frame(frame11, height=100, width=500, bg="#ffb16e")
search_frame.place(x=100, y=20)

search_text = Entry(search_frame, width=50, textvariable=search_var)
search_text.place(x=0, y=20)

search_b1 = Button(search_frame, text='Search', font='Verdana 10 bold', command=search)
search_b1.place(x=320, y=17)

view_b1 = Button(search_frame, text='View All', font='Verdana 10 bold', command=DisplayData)
view_b1.place(x=395, y=17)

table_frame = Frame(frame11, width=750, height=900, bg='black')
table_frame.place(x=20, y=100)

scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame, orient=VERTICAL)

student_table = ttk.Treeview(table_frame,
                             columns=("Full name", "Email Id", "Phone no.", "Gender", "Registration no.", "Branch",
                                      "Year", "CGPA", "CET/JEE", "Company Name"))
student_table.place(x=30, y=150)
student_table['show'] = 'headings'

student_table.heading('Full name', text='Full name')
student_table.heading('Email Id', text='Email Id')
student_table.heading('Phone no.', text='Phone no.')
student_table.heading('Gender', text='Gender')
student_table.heading('Registration no.', text='Registration no.')
student_table.heading('Branch', text='Branch')
student_table.heading('Year', text='Year')
student_table.heading('CGPA', text='CGPA')
student_table.heading('CET/JEE', text='CET/JEE')
student_table.heading('Company Name', text='Company Name')

student_table.pack()
student_table['show'] = 'headings'

student_table.column('Full name', width=70, minwidth=70)
student_table.column('Email Id', width=70, minwidth=70)
student_table.column('Phone no.', width=70, minwidth=70)
student_table.column('Gender', width=70, minwidth=70)
student_table.column('Registration no.', width=70, minwidth=70)
student_table.column('Branch', width=70, minwidth=70)
student_table.column('CGPA', width=70, minwidth=70)
student_table.column('Year', width=70, minwidth=70)
student_table.column('CET/JEE', width=70, minwidth=70)
student_table.column('Company Name', width=70, minwidth=70)

vsb = ttk.Scrollbar(window, orient="vertical", command=student_table.yview)
vsb.place(x=1230, y=235, height=200 + 20)

hsb = ttk.Scrollbar(window, orient="horizontal", command=student_table.xview)
hsb.place(x=430, y=535, width=700, height=20 + 0)

student_table.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

conn = sqlite3.connect('registration_student.db')
cur = conn.cursor()

# Create the "student_table" table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS student_table (
               Full_name TEXT,
               Email_Id TEXT,
               Phone_no TEXT,
               Gender TEXT,
               Registration_no TEXT PRIMARY KEY,
               Branch TEXT,
               Year TEXT,
               CGPA REAL,
               CET_JEE INTEGER,
               Company_Name TEXT
               )''')

# Commit changes and close the connection
conn.commit()
conn.close()

DisplayData()

window.geometry("1250x700")
window.config(bg="#FFF5B8")
window.mainloop()