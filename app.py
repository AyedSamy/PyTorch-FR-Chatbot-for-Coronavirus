# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:10:18 2021

@author: Samy Ayed
"""

from get_response import get_response
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    userMessage = request.get_data().decode("utf-8")
    return get_response(userMessage)


if __name__ == '__main__':
    app.run(debug=True)