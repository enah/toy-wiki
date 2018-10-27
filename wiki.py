import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("CREATE TABLE if not exists contents (title TEXT, body TEXT)")
    c.execute("SELECT title, body from contents ORDER BY rowid DESC")
    entry = c.fetchone()
    conn.close()
    if entry:
        return render_template("index.html", title=entry[0], body=entry[1])
    return render_template("index.html", title="", body="")

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/clear")
def clear():
    print("Clear called")
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("DROP TABLE contents")
    c.execute("CREATE TABLE if not exists contents (title TEXT, body TEXT)")
    conn.close()
    return

@app.route("/save")
def save():
    print("Save called")
    a = request.args
    title = a.get("title")
    body = a.get("body")
    conn = sqlite3.connect('wiki.db')
    c = conn.cursor()
    c.execute("UPDATE TABLE contents (title, body) VALUES (" + title + "," + body + ")")
    conn.close()
    return

if __name__ == '__main__':
    app.run()
