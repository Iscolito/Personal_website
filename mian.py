# -*- coding = utf-8 -*-
# @Time : 2022/8/21 16:55
# @Author : Iscolito
# @File : mian.py
# @Software : PyCharm
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('homepage.html')


@app.route('/page1')
def page1():
    return render_template('home.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


if __name__ == '__main__':
    app.run()
