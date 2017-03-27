# coding=utf-8
from torngas.handler import WebHandler
from torngas.handler import ApiHandler

import json

class BaseHandler(WebHandler,ApiHandler):
    """
    do some your base things
    """
    userArr = {}
    userArr['userName'] = 'Alex kong'
    userArr['uid'] = '100'
    result = {}

    def checkLogin(self, username, pwd) :
        userArr = {}

        if username == 'admin' and pwd == '123456':
            userArr['userName'] = 'Alex kong'
            userArr['uid'] = '100'
            return userArr
        else:
            return  userArr

    def successResponse(self, result):
        response = {'status': 1, 'msg': 'ok', 'data': result}
        ApiHandler.write_api(self, response, False, True, 'json')

    def failResponse(self, msg=''):
        response = {'status': -1, 'msg': msg}
        ApiHandler.write_api(self, response, False, True, 'json')

