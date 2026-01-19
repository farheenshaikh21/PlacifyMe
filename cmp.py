import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter import messagebox
import os

window2 = Tk()

company_name_var = StringVar()
company_id_var = StringVar()
company_Phone_no_var = StringVar()
no_of_recruits_var = StringVar()
company_email_var = StringVar()
address = StringVar()
branch_var = StringVar()
year_var = StringVar()
ssc_var = StringVar()
hsc_var = StringVar()
cgpa_var = StringVar()
search_var = StringVar()
del_var = StringVar()

f1 = Frame(window2)
f1.place(x=300, y=20)

title = Label(f1, text="Company Registration And It's Criteria", font=("Time Roman", 30, "bold"), bg="white", padx=10,
              pady=10, relief=RIDGE, bd=10)
title.pack(fill="both")

f2 = Frame(window2, width=350, height=200, bg="#ffb16e")
f2.place(x=30, y=130)

plab = Label(text="Company Details:")
plab.place(x=30, y=115)
nameL = Label(f2, text='Company Name ', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
nameL.place(x=10, y=10)

nameE = Entry(f2, textvariable=company_name_var, width=25)
nameE.place(x=150, y=14)

idL = Label(f2, text='Company Id:', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
idL.place(x=10, y=60)

idE = Entry(f2, textvariable=company_id_var, width=25)
idE.place(x=150, y=64)

phoneL = Label(f2, text='Phone no.', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
phoneL.place(x=10, y=110)

phoneE = Entry(f2, textvariable=company_Phone_no_var, width=25)
phoneE.place(x=150, y=114)

emailL = Label(f2, text='Email id', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
emailL.place(x=10, y=160)

emailE = Entry(f2, textvariable=company_email_var, width=25)
emailE.place(x=150, y=164)

clab = Label(text="Company Criteria: ")
clab.place(x=30, y=340)

f3 = Frame(window2, width=350, height=300, bg="#ffb16e")
f3.place(x=30, y=361)

branch = Label(f3, text='Branch', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
branch.place(x=10, y=10)

branche = ttk.Combobox(f3, textvariable=branch_var)
branche['values'] = ("IT", "EXTC", "MECH", "ELECTRICAL", "COMP", "CHEMICAL", "ELECTRONICS")
branche.place(x=150, y=13)

year = Label(f3, text='Year', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
year.place(x=10, y=60)

yeare = ttk.Combobox(f3, textvariable=year_var)
yeare['values'] = ("TE", "BE", "MCA")
yeare.place(x=150, y=64)

recruits = Label(f3, text='No.of recruits', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
recruits.place(x=10, y=110)

recruitse = Entry(f3, textvariable=no_of_recruits_var, width=25)
recruitse.place(x=150, y=114)

hsc = Label(f3, text='HSC', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
hsc.place(x=10, y=160)

hsce = Entry(f3, textvariable=hsc_var, width=25)
hsce.place(x=150, y=164)

ssc = Label(f3, text='SSC', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
ssc.place(x=10, y=210)

ssce = Entry(f3, textvariable=ssc_var, width=25)
ssce.place(x=150, y=214)

cgpa = Label(f3, text='CGPA', padx=5, pady=5, font=('Arial', 12, "bold"), bg="#ffb16e", fg="white")
cgpa.place(x=10, y=260)

cgpae = Entry(f3, textvariable=cgpa_var, width=25)
cgpae.place(x=150, y=264)

# Establish SQLite connection and cursor
conn = sqlite3.connect("registration_student.db")
cur = conn.cursor()

# Create company_table if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS company_table (
    company_name TEXT,
    company_ID TEXT PRIMARY KEY,
    phone_no TEXT,
    no_recruitments TEXT,
    Email_id TEXT,
    branch TEXT,
    year TEXT,
    HSC TEXT,
    SSC TEXT,
    CGPA TEXT
)''')
conn.commit()


def next():
    window2.destroy()
    os.system('Admin_login.py')


def DisplayData():
    company_table.delete(*company_table.get_children())
    cur.execute("SELECT * FROM company_table")
    rows = cur.fetchall()
    for row in rows:
        company_table.insert('', END, values=row)



def submit():
    if company_id_var.get() == "":
        messagebox.showerror("Error", "Company ID is required")
        return

    cur.execute(
        "INSERT INTO company_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            company_name_var.get(),
            company_id_var.get(),
            company_Phone_no_var.get(),
            no_of_recruits_var.get(),
            company_email_var.get(),
            branch_var.get(),
            year_var.get(),
            hsc_var.get(),
            ssc_var.get(),
            cgpa_var.get()
        )
    )
    conn.commit()
    DisplayData()
    reset()



def update():
    cur.execute(
        "UPDATE company_table SET company_name=?, phone_no=?, no_recruitments=?, Email_id=?, branch=?, year=?, HSC=?, SSC=?, CGPA=? WHERE company_ID=?",
        (company_name_var.get(), company_Phone_no_var.get(), no_of_recruits_var.get(), company_email_var.get(),
         branch_var.get(), year_var.get(), hsc_var.get(), ssc_var.get(), cgpa_var.get(),
         company_id_var.get()))
    conn.commit()
    DisplayData()
    reset()


def cancel():
    window2.destroy()


def search():
    cur.execute("SELECT * FROM company_table WHERE company_ID=?", (search_var.get(),))
    rows = cur.fetchall()
    for row in rows:
        company_table.insert('', END, values=row)


def delete():
    cur.execute("DELETE FROM company_table WHERE company_ID=?", (company_id_var.get(),))
    conn.commit()
    messagebox.showinfo("Record deleted", f"{company_id_var.get()} this record is deleted Successfully")
    DisplayData()
    reset()


def reset():
    company_name_var.set("")
    company_id_var.set("")
    company_email_var.set("")
    branch_var.set("")
    year_var.set("")
    cgpa_var.set("")
    company_Phone_no_var.set("")
    no_of_recruits_var.set("")
    hsc_var.set("")
    ssc_var.set("")


button_frame = Frame(window2, bg='#fff5b8', height=100, width=400, padx=20)
button_frame.place(x=15, y=665)

sub_b1 = Button(button_frame, text='Submit', font='Verdana 10 bold', command=submit)
sub_b1.place(x=10, y=0)

can_b1 = Button(button_frame, text='Cancel', font='Verdana 10 bold', command=cancel)
can_b1.place(x=80, y=0)

upd_b1 = Button(button_frame, text='Update', font='Verdana 10 bold', command=update)
upd_b1.place(x=150, y=0)

dlt_b1 = Button(button_frame, text='Delete', font='Verdana 10 bold', command=delete)
dlt_b1.place(x=220, y=0)

reset_b1 = Button(button_frame, text='Reset', font='Verdana 10 bold', command=reset)
reset_b1.place(x=290, y=0)

frame11 = Frame(window2, width=840, height=500, bg="#ffb16e")
frame11.place(x=400, y=140)

next_b1 = Button(text='NEXT >>', font='Verdana 10 bold', command=next)
next_b1.place(x=1100, y=665)

search_frame = Frame(frame11, height=100, width=500, bg="#ffb16e")
search_frame.place(x=100, y=20)

search_text = Entry(search_frame, width=50, textvariable=search_var)
search_text.place(x=0, y=20)

search_b1 = Button(search_frame, text='Search', font='Verdana 10 bold', command=search)
search_b1.place(x=320, y=17)

view_b1 = Button(search_frame, text='View All', font='Verdana 10 bold', command=DisplayData)
view_b1.place(x=395, y=17)

table_frame = Frame(frame11, width=750, height=900)
table_frame.place(x=20, y=100)

scroll_x1 = Scrollbar(table_frame, orient=HORIZONTAL)
scroll_y1 = Scrollbar(table_frame, orient=VERTICAL)

company_table = ttk.Treeview(table_frame,
                             columns=("Company_name", "Company_ID", "Phone_no", "no_recruitments", "Email_id", "Branch", "Year", "HSC", "SSC", "CGPA"))
company_table.place(x=30, y=150)

company_table.heading('Company_name', text='company_name')
company_table.heading('Company_ID', text='company_ID')
company_table.heading('Phone_no', text='phone_no')
company_table.heading('no_recruitments', text='no_recruitments')
company_table.heading('Email_id', text='Email_id')
company_table.heading('Branch', text='branch')
company_table.heading('Year', text='year')
company_table.heading('HSC', text='HSC')
company_table.heading('SSC', text='SSC')
company_table.heading('CGPA', text='CGPA')

company_table.pack()
company_table['show'] = 'headings'

company_table.column('Company_name', width=100, minwidth=70)
company_table.column('Company_ID', width=70, minwidth=70)
company_table.column('Phone_no', width=70, minwidth=70)
company_table.column('no_recruitments', width=70, minwidth=70)
company_table.column('Email_id', width=150, minwidth=70)
company_table.column('Branch', width=70, minwidth=70)
company_table.column('Year', width=70, minwidth=70)
company_table.column('HSC', width=70, minwidth=70)
company_table.column('SSC', width=70, minwidth=70)
company_table.column('CGPA', width=70, minwidth=70)

vsb = ttk.Scrollbar(window2, orient="vertical", command=company_table.yview)
vsb.place(x=1230, y=235, height=200 + 20)

hsb = ttk.Scrollbar(window2, orient="horizontal", command=company_table.xview)
hsb.place(x=430, y=535, width=700, height=20 + 0)
company_table.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

company_table.pack(fill=BOTH, expand=True)

DisplayData()

window2.geometry("1250x750")
window2.config(bg="#fff5b8")
window2.mainloop()
