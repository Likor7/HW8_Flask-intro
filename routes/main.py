from app import app
from flask import render_template


@app.route('/')
def hello():
    return "hello world!"


@app.route('/calc/<int:first_number>/<int:second_number>')
def calculator(first_number, second_number):
    return render_template("index.html", sum=f"{first_number} + {second_number} = {first_number + second_number}")
