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
def response_json():
    request_time = int(round(time.time() * 1000))
    res = {"meta_info": {"code": 200, "msg": "successfully", "request_time": request_time},
           "response": {"items": [{"id": 1, "create_time": request_time, "update_time": request_time}],
                        "page_info": {"page": 1, "page_num": 15, "page_size": 10, "total": 145}}}
    return jsonify(res)


@root.route("/tesst", methods=['GET'])
def test():
    """
    连接数据库和redis测试
    :return:
    """
    from models.users import Users
    from models import redis_connent
    user = Users()
    aa = user.find_by_userinfo("admin")
    print(aa[0])
    r = redis_connent()
    r.hset(name=f"user:11111", key="key1", value="value")
    return {}
