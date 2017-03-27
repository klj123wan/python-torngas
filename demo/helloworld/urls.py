# !/usr/bin/env python
# -*- coding: utf-8 -*-
from torngas import Url, route

u = Url('helloworld.handlers')
urls = route(
    u(name='Index', pattern=r'/?', handler='main_handler.Main'),
    u(name='Login', pattern=r'/login/?', handler='login_handler.Main'),
    u(r'/project/list/?', 'project_handler.List'),
    u(r'/project/del/?', 'project_handler.Delete'),
    u(r'/project/put/?', 'project_handler.Put'),
    u(r'/project/add/?', 'project_handler.Add'),
    u(r'/rsync/add/?', 'rsync_handler.Add'),
    #u(name='ProjectList', pattern=r'project/list/?', handler='project_handler.List'),
)

