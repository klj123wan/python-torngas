# coding=utf-8

from ..handlers.base_handler import BaseHandler
from ..models.project_models import Project
from ..models.rsync_models import Rsync
import time

projectModel = Project()
rsyncModel = Rsync()

#项目添加和修改
class Add(BaseHandler):
    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        noPublish = rsyncModel.getNotPublishRsync()
        j = len(noPublish)

        #没有找到模板中格式化时间的方法暂时这样写吧
        for i in range(j):
            if noPublish[i].created > 0:
                noPublish[i].createdl = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(noPublish[i].created))


        self.render("admin/rsync_add.html", data=data,projects=self.projectAll(),noPublist=noPublish)

    def post(self, *args, **kwargs):
        data = {}
        data['userInfo'] = BaseHandler.userArr

        file = self.get_argument('file', "")
        desc = self.get_argument('desc', "")
        pid = self.get_argument('pid', "")
        projectInfo = projectModel.getProjectInfo(pid)
        if projectInfo[0].status == 0:
            BaseHandler.failResponse(self, '项目不存在')

        params = {'files': file, 'pid': pid, 'status': 0, 'description': desc,'project':projectInfo[0].path,
                  'username': data['userInfo']['userName'], 'uid': data['userInfo']['uid'], 'email':'konglingjian@gmail.com',
                  'userip':'127.0.0.1'}

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