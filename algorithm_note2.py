# -*- coding = utf-8 -*-
# @Time : 2022/8/23 17:08
# @Author : Iscolito
# @File : algorithm_note1.py
# @Software : PyCharm
import sys
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route('/')
def algorithm_note1():
    return render_template('algorithm_note2.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("Building website...")
        freezer.freeze()
    else:
        app.run(debug=True)
