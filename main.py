# main.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # Получаем текущие дату и время
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return render_template("index.html", current_time=current_time)

@app.route("/index1/")
def index1():
    return render_template("index1.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/index_info/")
def index_info():
    return render_template("index_info.html")

@app.route("/index_table/")
def index_table():
    return render_template("index_table.html")



if __name__ == "__main__":
    app.run(debug=True)
