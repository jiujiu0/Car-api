import os
import datetime

import psycopg2
from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder="static", static_url_path="/static")
    # json化时候不要对中文做编码
    app.config['JSON_AS_ASCII'] = False
    app.config['ENV'] = os.environ.get('ENV')

    # 设置用于提供文件的静态文件夹
    app.config['UPLOAD_FOLDER'] = 'uploads'

    # 数据库连接
    init_db_pool(app)

    # 统一 API Key 认证
    setup_api_key_auth(app)

    # 配置钩子
    setup_app(app)
    app.logger.info("【INFO】后端启动成功: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return app


def init_db_pool(app):
    """
        初始化数据库连接池
        :param app:
        :return:
    """
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
    # 创建数据库连接
    try:
        app.db = psycopg2.connect(app.config['DATABASE_URL'])
        print("成功连接到数据库!")
    except Exception as e:
        print(f"连接数据库失败: {e}")


def register_all_blueprint(app):
    """
        注册蓝图
        :param app:
        :return:
    """
    from website.Controller.AccountController import bp as account
    from website.View.home import bp as home
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(account, url_prefix='/account')


def setup_api_key_auth(app):
    """
    统一 API Key 认证，适用于所有 API 请求
    """
    API_KEY = os.getenv('SECRET_KEY', 'e_car_shop-000c077a9a424414f32d77a0e1767af93e1c6d1c')  # 读取环境变量或使用默认值

    @app.before_request
    def require_api_key():
        if request.path.startswith('/static'):  # 允许访问静态资源
            return

        # 在请求时请求头添加 X-API-KEY 字段
        api_key = request.headers.get("X-API-KEY")
        if not api_key or api_key != API_KEY:
            return jsonify({"message": "Unauthorized"}), 401


def setup_app(app):
    register_all_blueprint(app)
