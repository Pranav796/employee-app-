from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="root123",
    database="employee_db"
)

@app.route("/")
def home():
    cur = db.cursor()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    return render_template("index.html", employees=data)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]

        cur = db.cursor()
        cur.execute(
            "INSERT INTO employees(name,role) VALUES(%s,%s)",
            (name,role)
        )
        db.commit()

        return redirect("/")

    return render_template("add.html")

app.run(host="0.0.0.0", port=5000)
