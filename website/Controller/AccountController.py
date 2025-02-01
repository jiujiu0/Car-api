from flask import Blueprint
from website.Utils.ResultMessage import ResultMessage
from website.Database.neon import neon_query_raw

bp = Blueprint('account', __name__)


@bp.route('/test', methods=['GET'])
def test():
    return ResultMessage(message="Account API is working").success()


@bp.route('/query', methods=['GET'])
def query():
    try:
        # 查询 tm_clients 表的所有数据
        query_sql = "SELECT * FROM tm_clients"
        clients = neon_query_raw(query_sql)

        if clients:
            return ResultMessage(data=clients).success()
        else:
            return ResultMessage('查询为空').fail()
    except Exception as e:
        return ResultMessage(f'sql报错：{e}').fail()
