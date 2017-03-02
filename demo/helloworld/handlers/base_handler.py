# coding=utf-8
from torngas.handler import WebHandler
from torngas.handler import ApiHandler


class BaseHandler(WebHandler):
    """
    do some your base things
    """
    userArr = {}
    userArr['userName'] = 'Alex kong'
    userArr['uid'] = '100'

    def checkLogin(self, username, pwd) :
        userArr = {}

        if username == 'admin' and pwd == '123456':
            userArr['userName'] = 'Alex kong'
            userArr['uid'] = '100'
            return userArr
        else:
            return  userArr
