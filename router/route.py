# -*- coding=utf-8 -*-
from flask import Flask, jsonify
import yaml
import os

__BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


def analysis_yaml():
    f = open(os.path.join(__BASE_DIR, "example", "devops.yaml"))
    x = yaml.load(f, Loader=yaml.FullLoader)
    im_n = x["artifacts"]["image"]
    im_v = x["artifacts"]["version"]
    im_tag = im_n[0] + ":" + str(im_v)
    print(im_tag)
    return x


# 定制404返回页面
@app.errorhandler(404)
def page_not_found(e):
    res = {"status": {"code":404,"msg":"404 Not Found"}}
    return jsonify(res), 404


@app.errorhandler(500)
def server_error(e):
    res = {"status": {"code": 500, "msg": "Internal server error"}}
    return jsonify(res), 500


@app.route("/", methods=['GET', 'HEAD'])
def index():
    res = {"status": {"code": 200, "msg": "successful"}}
    return jsonify(res)


@app.route("/yaml")
def hello_world():
    response = analysis_yaml()
    return jsonify(response)

@app.route("/ssl")
def certificate_detection():
    from ssl_cert.creating_ssl_certificates import signed_certificate
    res = signed_certificate()
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
