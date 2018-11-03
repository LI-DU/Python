from info import sr
from info.modules.home import home_blu
import logging  # python内置的日志模块  将日志信息在控制台中输出, 并且可以将日志保存到文件中
# flask中的默认日志也是集成的logging模块, 但是没有将日志保存到文件中
from flask import current_app, render_template


# 2.使用蓝图注册路由
@home_blu.route('/')
def index():

    return render_template("index.html")


@home_blu.route('/favicon.ico')
def favicon():
    # 网站小图标的请求是由浏览器自动发起的, 只需要实现该路由并返回图标对应图片即可
    # flask中内置了获取静态文件的语法send_static_file, flask访问静态文件的路由底层也是调用该方法
    return current_app.send_static_file("news/favicon.ico")