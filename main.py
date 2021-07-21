# -*- coding=utf-8 -*-
import os
from router.route import app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    app.run(debug=True)
