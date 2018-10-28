import sqlite3

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("SELECT title, body from contents ORDER BY rowid DESC")
    entry = c.fetchone()
    conn.close()
    if entry:
        return render_template("index.html", title=entry[0], body=entry[1])
    return render_template("index.html", title="No entries", body="")

@app.route("/edit")
def edit():
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("SELECT title, body from contents ORDER BY rowid DESC")
    entry = c.fetchone()
    conn.close()
    if entry:
        return render_template("edit.html", title=entry[0], body=entry[1])
    return render_template("edit.html", title="", body="")

@app.route("/history")
def history():
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    posts = [post for post in c.execute("SELECT title, body from contents ORDER BY rowid DESC")]
    conn.close()
    return render_template("history.html", posts=posts)

@app.route("/clear")
def clear():
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("DROP TABLE contents")
    c.execute("CREATE TABLE if not exists contents (title TEXT, body TEXT)")
    conn.commit()
    conn.close()
    return ""

@app.route("/save")
def save():
    a = request.args
    title = a.get("title")
    body = a.get("body")
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("INSERT INTO contents (title, body) VALUES (?, ?)", (title, body))
    conn.commit()
    conn.close()
    return ""

if __name__ == '__main__':
    app.run()
