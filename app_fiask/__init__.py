# -*- coding=utf-8 -*-
from urllib import request
from flask import Flask, request
import time

__app = Flask(__name__)


@__app.errorhandler(404)
def page_not_found(e):
    request_time = int(round(time.time() * 1000))
    msg = f"The requested URL {request.path} was not found on this server."
    return {"meta_info": {"code": 404, "msg": msg, "request_time": request_time}}, 404


@__app.errorhandler(500)
def server_error(e):
    request_time = int(round(time.time() * 1000))
    return {"meta_info": {"code": 500, "msg": "Internal server error", "request_time": request_time}}, 500


def init_app():
    return __app
