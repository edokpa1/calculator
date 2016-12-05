# -*- coding: utf-8 -*-
"""
    Calculator
    ~~~~~~~~~~~~~~

    A simple Calculator made by Flask and jQuery.

    :copyright: (c) 2015 by Grey li.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    a = request.args.get('num1', '0')
    operator = request.args.get('operator', '')
    b = request.args.get('num2', '0')
    if operator == '/':
        result = eval(a + operator + str(float(b)))
    else:
        result = eval(a + operator + b)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)