# coding=utf-8

from ..handlers.base_handler import BaseHandler
from ..models.project_models import Project

class Main(BaseHandler):

    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        self.render("admin/index.html", data=data)

# 项目列表
class List(BaseHandler):
    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        project = Project()
        project_list = project.GetProjectByCondition(self)
        self.render("admin/project_list.html", data=data,project_list=project_list)

# 项目删除
class Delete(BaseHandler):
    def get(self):
        id = self.get_argument('id')
        status = self.get_argument('status')
        project = Project()
        updateStatus = project.updateProjectStatus(id, status)
        if updateStatus == 1:
            self.redirect('/project/list')
        else:
            self.finish('fail')


#项目添加和修改
class Add(BaseHandler):
    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        self.render("admin/project_add.html", data=data)

    def post(self, *args, **kwargs):
        name = self.get_argument('projectName', "")
        codeCheck = self.get_argument('codeCheck', 0)
        checkEmail = self.get_argument('checkEmail', "")
        projectPath = self.get_argument('projectPath', "")
        gitPath = self.get_argument('gitPath', "")
        serverAddress = self.get_argument('serverAddress', "")
        if name == "" or projectPath == "" or gitPath == "" or serverAddress == "":
            self.redirect('/project/add')
        params = {'name':name, 'checkcode':codeCheck, 'checkemail':checkEmail, 'path':projectPath, 'git_path':gitPath,
                  'status':1, 'server_address':serverAddress}
        project = Project()
        insertStatus = project.addProject(params)
        if insertStatus == 1:
            self.redirect('/project/list')
        else:
            self.finish('fail')

class Put(BaseHandler):
    def get(self):
        data = {}
        data['userInfo'] = BaseHandler.userArr
        id = self.get_argument('id', 0)
        if id == 0:
            self.redirect('/project/list')

        projectModel = Project()
        project = projectModel.getProjectInfo(id)
        self.render("admin/project_edit.html", data=data, project=project[0])

    def post(self, *args, **kwargs):
        id = self.get_argument('id', 0)
        if id == 0:
            self.redirect('/project/list')

        name = self.get_argument('projectName', "")
        codeCheck = self.get_argument('codeCheck', 0)
        checkEmail = self.get_argument('checkEmail', "")
        projectPath = self.get_argument('projectPath', "")
        gitPath = self.get_argument('gitPath', "")

        if name == "" or projectPath == "" or gitPath == "":
            self.redirect('/project/put?id=' + id )

        params = {'name': name, 'checkcode': codeCheck, 'checkemail': checkEmail, 'path': projectPath,
                  'git_path': gitPath, 'status': 1}
        project = Project()
        addStatus = project.addProject(params, id)
        if addStatus == 1:
            self.redirect('/project/list')
        else:
            self.finish('fail')
