# -*- coding=utf-8 -*-

# redis
REDIS_HOST = "10.10.10.10"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_MAX_CONNECTIONS = 50

# db
DB_HOST = "10.10.10.10"
DB_PORT = 3306
DB_NAME = "consolemg"
DB_USER_NAME = "abc"
DB_PASSWD = 123456

# 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）
SQLALCHEMY_POOL_SIZE = 100
# 控制在连接池达到最大值后可以创建的连接数。当这些额外的连接使用后回收到连接池后将会被断开和抛弃。保证连接池只有设置的大小
SQLALCHEMY_MAX_OVERFLOW = 100
# 自动回收连接的秒数。这对MySQL是必须的，默认情况下MySQL会自动移除闲置8小时或者以上的连接,Flask-SQLAlchemy会自动地设置这个值为 2 小时
SQLALCHEMY_POOL_RECYCLE = 1200
# 如果设置成 True，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助;默认为false；
SQLALCHEMY_ECHO = True
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False
