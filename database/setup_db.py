import sqlite3

con = sqlite3.connect("registration_student.db")
cur = con.cursor()

# STUDENT SIGNUP
cur.execute("""
CREATE TABLE IF NOT EXISTS student_signUP (
    name TEXT NOT NULL,
    student_id TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# STUDENT DETAILS
cur.execute("""
CREATE TABLE IF NOT EXISTS student_table (
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
)
""")

# COMPANY LOGIN
cur.execute("""
CREATE TABLE IF NOT EXISTS company_login (
    name TEXT NOT NULL,
    id TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

# ADMIN LOGIN
cur.execute("""
CREATE TABLE IF NOT EXISTS admin (
    user_name TEXT PRIMARY KEY,
    Password TEXT NOT NULL
)
""")

# DEFAULT ADMIN
cur.execute("""
INSERT OR IGNORE INTO admin (user_name, Password)
VALUES ('admin', 'admin123')
""")

con.commit()
con.close()

print("Database setup completed successfully!")
