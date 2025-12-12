from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "myattendanceapp2025"  # <-- proper secret key

DB_NAME = "attendance.db"

# ----------------- DB Helpers -----------------
def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    c = conn.cursor()

    # Students table
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL
        )
    """)

    # Attendance table
    c.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT NOT NULL,
            name TEXT NOT NULL,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            UNIQUE(roll, day)
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------------- Routes -----------------

# Student page
@app.route("/", methods=["GET","POST"])
def student_page():
    msg = ""
    if request.method == "POST":
        roll = request.form.get("roll", "").strip()

        conn = get_conn()
        c = conn.cursor()
        c.execute("SELECT name FROM students WHERE roll=?", (roll,))
        student = c.fetchone()

        if student:
            name = student[0]
            today = date.today().strftime("%Y-%m-%d")
            now_time = datetime.now().strftime("%H:%M:%S")

            try:
                c.execute("INSERT INTO attendance (roll,name,day,time) VALUES (?,?,?,?)",
                          (roll,name,today,now_time))
                conn.commit()
                msg = f"Attendance marked for {name} ({roll})"
            except sqlite3.IntegrityError:
                msg = "You already marked attendance today."
        else:
            msg = "Roll not registered."

        conn.close()

    return render_template("student.html", msg=msg)

# Teacher login
@app.route("/login", methods=["GET","POST"])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "teacher" and password == "password123":
            session["teacher"] = True
            return redirect(url_for("view_attendance"))
        else:
            msg = "Invalid credentials"
    return render_template("login.html", msg=msg)

@app.route("/logout")
def logout():
    session.pop("teacher", None)
    return redirect(url_for("login"))

def require_teacher():
    return "teacher" in session

# View Attendance
@app.route("/view")
def view_attendance():
    if not require_teacher():
        return redirect(url_for("login"))

    today = date.today().strftime("%Y-%m-%d")
    conn = get_conn()
    c = conn.cursor()
    try:
        c.execute("SELECT id, roll, name, day, time FROM attendance WHERE day=? ORDER BY time DESC", (today,))
        records = c.fetchall()
    except sqlite3.OperationalError:
        records = []
    conn.close()
    return render_template("view.html", records=records)

# Clear Attendance
@app.route("/clear")
def clear_attendance():
    if not require_teacher():
        return redirect(url_for("login"))

    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM attendance")
    conn.commit()
    conn.close()
    return redirect(url_for("view_attendance"))

# Register Student
@app.route("/register", methods=["GET","POST"])
def register_student():
    if not require_teacher():
        return redirect(url_for("login"))

    msg = ""
    if request.method == "POST":
        roll = request.form.get("roll", "").strip()
        name = request.form.get("name", "").strip()

        conn = get_conn()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO students (roll,name) VALUES (?,?)", (roll,name))
            conn.commit()
            msg = f"Student {name} ({roll}) registered successfully!"
        except sqlite3.IntegrityError:
            msg = "Roll already exists!"
        conn.close()
    return render_template("register.html", msg=msg)

# ----------------- Run Server -----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
