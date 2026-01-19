from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


def display_companies():
    conn = sqlite3.connect('registration_student.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM company_table")

    result = cur.fetchall()
    conn.close()

    if len(result) != 0:
        company_info.delete(1.0, END)
        for row in result:
            company_info.insert(END, f"Company: {row[0]}\n")
            company_info.insert(END, f"No. of recruitments: {row[3]}\n")
            company_info.insert(END, f"Branch criteria: {row[5]}\n")
            company_info.insert(END, f"Minimum CGPA: {row[9]}\n\n")
    else:
        company_info.delete(1.0, END)
        company_info.insert(END, "No upcoming companies scheduled.")


window_student = Tk()
window_student.title("Student Dashboard")
window_student.geometry("600x400")
window_student.config(bg="#fff5b8")

# Frame for company information
frame_company = Frame(window_student, bg="#fff5b8")
frame_company.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Label for company information
label_company = Label(frame_company, text="Upcoming Companies", font=("Verdana", 16, "bold"), bg="#fff5b8", fg="black")
label_company.pack(pady=(10, 5))

# Text widget to display company information
company_info = Text(frame_company, wrap=WORD, bg="white", font="Verdana 10", bd=2, relief="solid", padx=5, pady=5)
company_info.pack(fill=BOTH, expand=True)

# Frame for buttons
frame_buttons = Frame(window_student, bg="#fff5b8")
frame_buttons.pack(pady=10)

display_companies()  # Initial display of company information

window_student.mainloop()