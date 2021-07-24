# -*- coding=utf-8 -*-
from flask import Blueprint, jsonify

cert = Blueprint('cert', __name__)


@cert.route("/ssl")
def certificate_detection():
    """
    :return:
    """
    from ssl_cert.creating_ssl_certificates import signed_certificate
    res = signed_certificate()
    return jsonify(res)
