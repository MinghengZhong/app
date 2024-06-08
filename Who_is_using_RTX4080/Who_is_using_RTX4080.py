import os
from flask import Flask, render_template
import psutil

app = Flask(__name__)


def check_remote_control():
    # 获取当前所有活动的用户会话
    sessions = psutil.users()

    # 检查每个用户会话的终端类型
    for session in sessions:
        # 如果终端类型为'rdp'，则表示是远程桌面会话
        if session.terminal == 'rdp':
            return True

    # 如果没有发现远程桌面会话，则返回 False
    return False


def get_current_user():
    # 获取当前登录的用户名
    return os.getlogin()


@app.route('/')
def index():
    remote_control = check_remote_control()
    if not remote_control:
        message = "没人在用RTX4080"
    else:
        current_user = get_current_user()
        message = f"{current_user}正在使用RTX4080"
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
