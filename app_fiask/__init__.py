from flask import Flask

__app = Flask(__name__)
def init_app():
    @__app.route("/", methods=['GET', 'HEAD'])
    def index():
        return {"status": {"code": 200, "msg": "successful"}}
    return __app


# 404
@__app.errorhandler(404)
def page_not_found(e):
    return {"status": {"code":404,"msg":"404 Not Found"}}, 404

# 500
@__app.errorhandler(500)
def server_error(e):
    return {"status": {"code": 500, "msg": "Internal server error"}}, 500

