# -*- coding = utf-8 -*-
# @Time : 2022/8/21 22:44
# @Author : Iscolito
# @File : blog.py
# @Software : PyCharm
import sys
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route('/')
def main_page():
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

        
