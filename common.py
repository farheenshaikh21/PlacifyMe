from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import os

window=Tk()

submit_var = StringVar()


def submit():
    e = submit_var.get()

    if e == "Student":
        window.destroy()
        #import std_login
        os.system('std_login.py')

    elif e == "Company":
        window.destroy()
        #import cmp_login
        os.system('cmp_login.py')

    elif e == "Admin":
        window.destroy()
        #import Admin_login
        os.system('Admin_login.py')

    else:
        messagebox.showerror("","Sorry,You dont have access to the system")


def cancel():
    window.destroy()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, "assets", "placementcell.png")

icon = PhotoImage(file=ICON_PATH)
window.iconphoto(True, icon)
window.icon = icon



labelphoto = Label(window,image=icon)
labelphoto.pack()



lab = Label(window,text='USER TYPE',font='Verdana 10 bold',bg="#fff5b8",fg='black')
lab.place(y=265,x=60)

entry = ttk.Combobox(window,textvariable=submit_var,width=40)
entry['values'] = ("Student","Company","Admin")
entry.place(y=270,x=200)
#
button_frame = Frame(window,height=100,width=200,padx=20,bg='#fff5b8')
button_frame.place(x=180,y=300)

submit = Button(button_frame,text='Submit',font='Verdana 10 bold',command=submit)
submit.place(x=10,y=20)

cancel = Button(button_frame,text='Cancel',font='Verdana 10 bold',command=cancel)
cancel.place(x=100,y=20)



window.title("Home Page")

window.geometry("600x500")
window.config(bg="#fff5b8")
window.mainloop()
