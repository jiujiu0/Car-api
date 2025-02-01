import os
from website import create_app
from dotenv import load_dotenv

os.environ['ENV'] = 'DEV'
load_dotenv('.env.dev')
app = create_app()
app.config.from_prefixed_env()
app.config['SECRET_KEY'] = os.urandom(24)

# 禁用自动重载以加速启动
app.run(use_reloader=False, port=25022)
