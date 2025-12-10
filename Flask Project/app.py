from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


#DATABASE
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


init_db()


#ROUTES

@app.route('/')
def home():
    return redirect("/login")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                        (username, password))
            conn.commit()
        except:
            return "Username already exists!"
        conn.close()
        return redirect("/login")

    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password!"

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)