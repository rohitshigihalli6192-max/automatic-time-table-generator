from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# ---------- Step 1: Database Setup ----------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    code TEXT UNIQUE NOT NULL,
                    department TEXT NOT NULL,
                    semester INTEGER NOT NULL
                )''')
    conn.commit()
    conn.close()

# Call the database setup function
init_db()

# ---------- Step 2: Routes ----------
@app.route('/')
def home():
    return "✅ Flask app running successfully!"

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/add_course', methods=["GET", "POST"])
def add_course():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        code = request.form["code"]
        department = request.form["department"]
        semester = request.form["semester"]

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO courses (name, code, department, semester) VALUES (?, ?, ?, ?)",
                      (name, code, department, semester))
            conn.commit()
            message = "✅ Course added successfully!"
        except sqlite3.IntegrityError:
            message = "⚠️ Course code already exists!"
        finally:
            conn.close()

    return render_template("add_course.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
