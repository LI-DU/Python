from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置数据库的连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/book_test"
# 设置是否追踪数据库变化 (一旦开启, 非常消耗性能)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "test"

db = SQLAlchemy(app)

#作者表


@app.route('/')
def index():

    return "index"

if __name__ == '__main__':
    app.run(debug=True)

