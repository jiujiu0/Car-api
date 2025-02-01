from flask import Flask
from website.Controller.AccountController import bp

# 创建 Flask 应用
app = Flask(__name__)

# 注册 Blueprint
app.register_blueprint(bp, url_prefix='/account')

# 测试运行
if __name__ == '__main__':
    app.run(debug=True)