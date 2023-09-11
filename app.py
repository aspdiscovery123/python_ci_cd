# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:58:06 2023

@author: aspdi
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
