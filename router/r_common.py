# -*- coding=utf-8 -*-
from flask import jsonify, Blueprint
import yaml
import os

__BASE_DIR = os.path.dirname(os.path.abspath(__file__))
common = Blueprint('common', __name__)


def analysis_yaml():
    f_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "example", "devops.yaml")
    f = open(f_path)
    x = yaml.load(f, Loader=yaml.FullLoader)
    im_n = x["artifacts"]["image"]
    im_v = x["artifacts"]["version"]
    im_tag = im_n[0] + ":" + str(im_v)
    print(im_tag)
    return x


@common.route("/yaml")
def hello_world():
    """
    /api/v1/common/yaml
    :return:
    """
    response = analysis_yaml()
    return jsonify(response)
