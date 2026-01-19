from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


def DisplayData3():
    conn = sqlite3.connect('registration_student.db')
    cur = conn.cursor()

    selected.delete(*selected.get_children())

    selection = search_var.get()

    if selection == "Student":
        headings = ("name", "email", "phone", "gender",
                    "reg_no", "branch", "year", "cgpa", "cet_jee", "company")

        selected["columns"] = headings
        selected.heading("#0", text="")

        for h in headings:
            selected.heading(h, text=h)

        cur.execute("""
            SELECT Full_name, Email_Id, Phone_no, Gender,
                   Registration_no, Branch, Year, CGPA, CET_JEE, Company_Name
            FROM student_table
        """)

    elif selection == "Company":
        headings = ("company_name", "company_id", "phone",
                    "email", "branch", "year", "recruiters", "cet_jee", "cgpa")

        selected["columns"] = headings
        selected.heading("#0", text="")

        for h in headings:
            selected.heading(h, text=h)

        cur.execute("""
            SELECT company_name, company_ID, phone_no, no_recruitments,
                   Email_id, branch, year, HSC, SSC, CGPA
            FROM company_table
        """)

    elif selection == "Selected Student":
        headings = ("name", "email", "phone", "gender",
                    "reg_no", "branch", "year", "cgpa", "cet_jee", "company")

        selected["columns"] = headings
        selected.heading("#0", text="")

        for h in headings:
            selected.heading(h, text=h)

        cur.execute("""
            SELECT Full_name, Reg_no, Company_name, CGPA, Sector, Year_of_joining
            FROM selected_student
        """)

    rows = cur.fetchall()

    if rows:
        for row in rows:
            selected.insert('', END, values=row)
    else:
        messagebox.showinfo("Info", "No records found")

    conn.close()


def add_to_selected():
    selected_item = selected.focus()
    if selected_item:
        item_values = selected.item(selected_item, 'values')
        conn = sqlite3.connect('registration_student.db')
        cur = conn.cursor()
        try:
            cur.execute("""
    INSERT INTO selected_student
    (Full_name, Reg_no, Company_name, CGPA, Sector, Year_of_joining)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    item_values[0],   # Full_name
    item_values[4],   # Registration_no 
    item_values[9],   # Company_Name
    item_values[7],   # CGPA
    item_values[5],   # Sector
    item_values[6]    # Year_of_joining
))
            conn.commit()
            messagebox.showinfo("", "Student added to selected student list")
            DisplayData3()
        except sqlite3.Error as e:
            conn.rollback()
            messagebox.showerror("Error", f"Failed to add student to selected student list: {e}")
        finally:
            conn.close()


def view_selected_students():
    conn = sqlite3.connect('registration_student.db')
    cur = conn.cursor()

    selected.delete(*selected.get_children())  # Clear existing data

    cur.execute("SELECT * FROM selected_student")
    result = cur.fetchall()
    conn.close()

    if len(result) != 0:
        for row in result:
            selected.insert('', END, values=row)
    else:
        messagebox.showinfo("Selected Students", "No selected students found")



def apply_filter():
    conn = sqlite3.connect('registration_student.db')
    cur = conn.cursor()

    selected.delete(*selected.get_children())  # Clear existing data

    branch = branch_var.get()
    min_cgpa = cgpa_var.get()

    cur.execute("SELECT * FROM student_table WHERE Branch=? AND CGPA >= ?", (branch, min_cgpa))

    result = cur.fetchall()
    if len(result) != 0:
        for row in result:
            selected.insert('', END, values=row)
    else:
        messagebox.showinfo("", "No records found")

    conn.close()


window3 = Tk()
window3.title("Main Window")

search_var = StringVar()
search_var.set("Student")  # Default selection

frame13 = Frame(window3, width=840, height=450, bg="#fff5b8")
frame13.pack(fill=BOTH, expand=True)

search_frame3 = Frame(frame13, height=100, bg="#fff5b8")
search_frame3.pack(side=TOP, pady=10)

search_text = ttk.Combobox(search_frame3, width=50, textvariable=search_var)
search_text['values'] = ("Student", "Company", "Selected Student")
search_text.pack(side=LEFT, padx=10)

search_b3 = Button(search_frame3, text='Search', font='Verdana 10 bold', command=DisplayData3)
search_b3.pack(side=LEFT, padx=10)

view_b1 = Button(search_frame3, text='View All', font='Verdana 10 bold', command=DisplayData3)
view_b1.pack(side=LEFT, padx=10)

table_frame3 = Frame(frame13, bg='black')
table_frame3.pack(fill=BOTH, expand=True)

scroll_x = Scrollbar(table_frame3, orient=HORIZONTAL)
scroll_y = Scrollbar(table_frame3, orient=VERTICAL)

selected = ttk.Treeview(table_frame3, height=14,
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
selected.pack(fill=BOTH, expand=True)

scroll_x.config(command=selected.xview)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.config(command=selected.yview)
scroll_y.pack(side=RIGHT, fill=Y)

buttons_frame = Frame(window3, bg="#fff5b8")
buttons_frame.pack(side=BOTTOM, fill=X)

add_to_selected_button = Button(buttons_frame, text='Add to Selected', font='Verdana 10 bold', command=add_to_selected)
add_to_selected_button.pack(side=LEFT, padx=10, pady=10)

filter_button = Button(buttons_frame, text='Filter Students', font='Verdana 10 bold', command=apply_filter)
filter_button.pack(side=LEFT, padx=10, pady=10)

view_selected_button = Button(buttons_frame, text='View Selected Students', font='Verdana 10 bold',
                              command=view_selected_students)
view_selected_button.pack(side=LEFT, padx=10, pady=10)


# Additional widgets for filtering by Branch and CGPA
filter_frame = Frame(window3, bg="#fff5b8")
filter_frame.pack(side=BOTTOM, fill=X)

# Additional widgets for filtering by Branch and CGPA
branch_label = Label(filter_frame, text="Branch:", bg="#fff5b8")
branch_label.pack(side=LEFT, padx=10, pady=10)

branch_var = StringVar()
branch_entry = Entry(filter_frame, textvariable=branch_var)
branch_entry.pack(side=LEFT, padx=10, pady=10)

cgpa_label = Label(filter_frame, text="Minimum CGPA:", bg="#fff5b8")
cgpa_label.pack(side=LEFT, padx=10, pady=10)

cgpa_var = DoubleVar()
cgpa_entry = Entry(filter_frame, textvariable=cgpa_var)
cgpa_entry.pack(side=LEFT, padx=10, pady=10)

window3.geometry("1000x750")
window3.config(bg="#ffb16e")
window3.mainloop()

