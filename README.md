# Placement Management System

A **Python + Tkinter + SQLite based Placement Management System** designed to manage student registrations, company details, and placement selections for a college placement cell.

This project provides separate modules for **Admin**, **Students**, and **Companies**, allowing smooth handling of placement-related data through a graphical user interface.

---

## 🚀 Features

### 👨‍🎓 Student Module

* Student signup and login
* Student registration with academic details
* View registered details
* View upcoming companies

### 🏢 Company Module

* Company signup and login
* Add and update company details
* View eligible students

### 🛠 Admin Module

* Admin login
* View all students and companies
* Manage selected students

### 📊 Database

* Uses **SQLite** for lightweight, file-based storage
* Automatic table creation if not present

---

## 🗂 Project Structure

```
PlacifyMe/
│
├── assets/
│   └── placementcell.png
│
├── database/
│   └── setup_db.py
│
├── Admin_login.py
├── cmp.py
├── cmp_login.py
├── cmp_signup.py
├── cmp_up.py
├── common.py
├── selected.py
├── std_login.py
├── std_signup.py
├── student.py
├── view.py
│
├── .gitignore
└── README.md
```

---

## 🗄 Database Tables

The project uses the following SQLite tables:

* `admin`
* `student_signUP`
* `student_table`
* `company_login`
* `company_table`
* `selected_student`

All tables are created automatically using setup scripts or during runtime.

---

## ⚙️ Technologies Used

* **Python 3**
* **Tkinter** (GUI)
* **SQLite3** (Database)
* **DB Browser for SQLite** (for database inspection – optional)

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites

* Python 3.x installed
* No external libraries required

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/placement-management-system.git
cd placement-management-system
```

### 3️⃣ Run the Application

Start from the common entry file:

```bash
python common.py
```

> ⚠️ **Note:**
>
> * Close one window before opening another
> * Do not run the same file multiple times simultaneously (avoids database lock issues)

---

## 🧪 Sample Admin Credentials

> Admin credentials are stored inside the database.
> Use **DB Browser for SQLite** to view or update them if required.

---

## 📌 Important Notes

* Database file: `registration_student.db`
* Ensure this file is in the same directory as the Python files
* Do not rename database tables or columns

---

## 📷 Screenshots

(Add screenshots here if required)

---


