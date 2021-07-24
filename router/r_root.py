# -*- coding=utf-8 -*-
from flask import Blueprint, jsonify
import time

root = Blueprint('root', __name__)


@root.route("/", methods=['GET', 'HEAD'])
def index():
    """
    接口检测，健康检测等
    :return:
    """
    request_time = int(round(time.time() * 1000))
    return {"meta_info": {"code": 200, "msg": "successfully", "request_time": request_time}}


@root.route("/response/json", methods=['GET'])
def test():
    request_time = int(round(time.time() * 1000))
    res = {"meta_info": {"code": 200, "msg": "successfully", "request_time": request_time},
           "response": {"items": [{"id": 1, "create_time": request_time, "update_time": request_time}],
                        "page_info": {"page": 1, "page_num": 15, "page_size": 10, "total": 145}}}
    return jsonify(res)
