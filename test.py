from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config:   #　定义配置类　封装所有的配置，方便对配置统一的管理
    # 定义和配置同名的类属性
    DEBUG = True #　设置调试模式
    #　配置数据库连接地址
    SQLALCHEMY_TRACK_MODIFICATIONS = "mysql://root:mysql@127.0.0.1:3306/info19"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 设置追踪数据库变化

# 从对象加载配置信息
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()