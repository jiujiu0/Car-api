from flask import *

bp = Blueprint('main_view', __name__)


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    return "success"
