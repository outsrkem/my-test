# -*- coding=utf-8 -*-
from sqlalchemy import MetaData
import redis


def dbconnect():
    from app_fiask import db
    dbsession = db.session
    dbmodel = db.Model
    metadata = MetaData(bind=db.engine)
    return dbsession, dbmodel, metadata


def redis_connent():
    from settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_MAX_CONNECTIONS
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, db=REDIS_DB,
                                max_connections=REDIS_MAX_CONNECTIONS)
    red = redis.Redis(connection_pool=pool)
    return red
