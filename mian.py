# -*- coding = utf-8 -*-
# @Time : 2022/8/21 16:55
# @Author : Iscolito
# @File : mian.py
# @Software : PyCharm
import sys
from flask import Flask, render_template
from flask_frozen import Freezer
# 实际对应的包为Frozen_Flask

app = Flask(__name__)
freezer = Freezer(app)


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
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building website...")
        freezer.freeze()
    else:
        app.run(debug=True)
