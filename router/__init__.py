# -*- coding=utf-8 -*-
from flask import Flask
from .r_cert import cert as cert
from .r_common import common as common



def reg_blueprint(app):
    """
    注册蓝图,所有接口前缀都在这里
    :param app:
    """
    app.register_blueprint(cert, url_prefix='/api/v1/cert')
    app.register_blueprint(common, url_prefix='/api/v1/common')
