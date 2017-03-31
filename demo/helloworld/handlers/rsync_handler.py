# coding=utf-8
from ..handlers.base_handler import BaseHandler
from ..models.project_models import Project
from ..models.rsync_models import Rsync
from ..models.redis_models import Redis

import time


projectModel = Project()
rsyncModel = Rsync()
redisModel = Redis()


PROJECT_PATH = "/data/www/python/"

#项目添加和修改
class Add(BaseHandler):
    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        noPublish = rsyncModel.getNotPublishRsync()
        j = len(noPublish)

        #没有找到模板中格式化时间的方法暂时这样写吧
        for i in range(j):
            noPublish[i].fileCount = len(noPublish[i].files.split("\n"))
            if noPublish[i].created > 0:
                noPublish[i].createdl = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(noPublish[i].created))


        self.render("admin/rsync_add.html", data=data,projects=self.projectAll(),noPublist=noPublish)

    def post(self, *args, **kwargs):
        data = {}
        data['userInfo'] = BaseHandler.userArr

        file = self.get_argument('file', "")
        desc = self.get_argument('desc', "")
        pid = self.get_argument('pid', "")
        # 判断上面目录是否是禁止目录

        # 判断代码是否存在不能上线的内容

        projectInfo = projectModel.getProjectInfo(pid)
        if projectInfo[0].status == 0:
            BaseHandler.failResponse(self, '项目不存在')

        params = {'files': file, 'pid': pid, 'status': 0, 'description': desc,'project':projectInfo[0].path,
                  'username': data['userInfo']['userName'], 'uid': data['userInfo']['uid'], 'email':'konglingjian@gmail.com',
                  'userip':'127.0.0.1', 'tagid' : self.getRsyncTagId(pid)}

        rsyncModel.addRsync( params)
        BaseHandler.successResponse(self, 'ok')

    def projectAll(self):
        return projectModel.getNormalProjects()

    def checkProjectStatus(self, pid):
        projectInfo = projectModel.getProjectInfo(pid)
        status = 0
        if projectInfo[0].status == 1:
            status = 1
        return  status

    def getRsyncTagId(self,pid):
        rsyncInfo = rsyncModel.getLastRsync(pid)
        if len(rsyncInfo) == 0:
            return 1
        else:
            return rsyncInfo[0].tagid + 1

class Deploy(BaseHandler):

    def post(self):
        id = self.get_argument('id', "")
        rsyncInfo = rsyncModel.getRsyncInfo(id)
        if rsyncInfo[0].status != 0:
            BaseHandler.failResponse(self, '该条上线记录状态错误，不能上线')
        #rsyncModel.updateRsyncStatus(id, 1)
        redisModel.pushDeploy(id)
        BaseHandler.successResponse(self, 'ok')



