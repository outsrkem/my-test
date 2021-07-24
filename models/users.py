# -*- coding=utf-8 -*-
from models import dbconnect
from sqlalchemy import Table


dbsession, dbmodel, metadata = dbconnect()


class Users(dbmodel):
    __table__ = Table('user', metadata, autoload=True)

    @staticmethod
    def find_by_userinfo(username):
        result = dbsession.query(Users).filter_by(USERNAME=username).all()
        return result
