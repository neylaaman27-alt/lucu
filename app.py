from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

PASSWORD_ADMIN = "admin123"

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pesan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isi TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/kirim", methods=["POST"])
def kirim():
    pesan = request.form["pesan"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO pesan (isi) VALUES (?)", (pesan,))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form["password"]

        if password == PASSWORD_ADMIN:
            conn = sqlite3.connect("database.db")
            c = conn.cursor()
            c.execute("SELECT * FROM pesan ORDER BY id DESC")
            data = c.fetchall()
            conn.close()

            return render_template("admin.html", data=data, akses=True)
        else:
            return render_template("admin.html", akses=False)

    return render_template("admin.html", akses=False)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)