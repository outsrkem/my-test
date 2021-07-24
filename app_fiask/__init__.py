# -*- coding=utf-8 -*-
from urllib import request
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from settings import DB_HOST, DB_PORT, DB_NAME, DB_USER_NAME, DB_PASSWD
from settings import SQLALCHEMY_POOL_SIZE, SQLALCHEMY_POOL_RECYCLE, \
    SQLALCHEMY_TRACK_MODIFICATIONS, SQLALCHEMY_ECHO, SQLALCHEMY_MAX_OVERFLOW
import time

__app = Flask(__name__)
__app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{DB_USER_NAME}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'
__app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
__app.config['SQLALCHEMY_POOL_SIZE'] = SQLALCHEMY_POOL_SIZE
__app.config['SQLALCHEMY_POOL_RECYCLE'] = SQLALCHEMY_POOL_RECYCLE
__app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
__app.config['SQLALCHEMY_MAX_OVERFLOW'] = SQLALCHEMY_MAX_OVERFLOW
db = SQLAlchemy(__app)


@__app.errorhandler(404)
def page_not_found(e):
    request_time = int(round(time.time() * 1000))
    msg = f"{str(e)} URL: {request.path} "
    return {"meta_info": {"code": 404, "msg": msg, "request_time": request_time}}, 404


@__app.errorhandler(500)
def server_error(e):
    request_time = int(round(time.time() * 1000))
    return {"meta_info": {"code": 500, "msg": "Internal server error", "request_time": request_time}}, 500


def init_app():
    return __app
