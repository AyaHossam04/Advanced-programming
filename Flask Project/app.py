from flask import Flask, render_template, request, redirect, url_for
import sqlite3 #sql

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
def index():
    return redirect("/signup")

@app.route('/home')
def home():
    return render_template("home.html")

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
            conn.close()
            return redirect(url_for('home', username=username))
        except:
            conn.close()
            return "Username already exists!"
        
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
            return redirect(url_for('home', username=username))
        else:
            return "Invalid username or password!"
        
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)