# -*- coding=utf-8 -*-
from flask import Blueprint

root = Blueprint('root', __name__)


@root.route("/", methods=['GET', 'HEAD'])
def index():
    """
    接口检测，健康检测等
    :return:
    """
    return {"status": {"code": 200, "msg": "successful"}}
