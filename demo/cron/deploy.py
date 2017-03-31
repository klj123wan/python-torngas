#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.environ.setdefault('TORNGAS_APP_SETTINGS', 'demo.settings.setting')

from demo.helloworld.models.project_models import Project
from demo.helloworld.models.rsync_models import Rsync
from demo.helloworld.models.redis_models import Redis

#本地路径自己配置
LOCAL_PATH = "/data/www/python/"

projectModel = Project()
rsyncModel = Rsync()
redisModel = Redis()

def deploy():

    deployInfo = rsyncModel.getRsyncInfo(4)
    rsync(deployInfo[0])

    deployCount = redisModel.lenDeploy()
    if deployCount == 0:
        print 'ok'
        return ''

    rsid = redisModel.popDelpoy()

    if rsid == None:
        print 'ok'
        return ''

    deployInfo = rsyncModel.getRsyncInfo(rsid)
    print deployInfo

def rsync(info):
    project = projectModel.getProjectInfo(info.pid)
    server = project[0].server_address
    path = project[0].path
    localPath = LOCAL_PATH + project[0].name
    fileList = info.files.split("\n")
    #cd  到固定位置
    checkdir = " cd " + localPath

    checkdirStatus = os.system(checkdir)
    if checkdirStatus != 0:
        print "fail"
        return
    #git
    git = "git add . ; git commit -m '" +info.description +"' ; git tag " + str(info.tagid) + "; git pull"
    gitstatus = os.system(git)
    if gitstatus!= 0:
        print "git fail"
        return 

    if len(fileList) == 1:
        shell = "/usr/bin/rsync -av --password-file=/data/www/python/www.torngas.com/demo/cron/rsync.password  " + localPath + '/' + info.files + '  konglj@' + server + "::backup/" + path
        print shell
        print os.system(shell)
    else:
        for i in range(len(fileList)):
            shell = "/usr/bin/rsync -av --password-file=/data/www/python/www.torngas.com/demo/cron/rsync.password  " + localPath + '/' + fileList[i] + '  konglj@' + server + "::backup/" + path
            print shell

    return 1


deploy()