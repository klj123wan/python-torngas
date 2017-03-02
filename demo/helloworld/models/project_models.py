# -*-coding=utf8-*-
# your models module write here
import datetime
from torngas.db.dbalchemy import Model
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref


class BaseModel(Model):
    __abstract__ = True
    __connection_name__ = 'default'

    id = Column(Integer, primary_key=True, nullable=False)

class Project(BaseModel):

    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(32), nullable=False)
    status = Column(Integer, nullable=False)
    checkcode = Column(Integer, nullable=False)
    checkemail = Column(String(50), nullable=False)
    path = Column(String(30), nullable=False)
    git_path = Column(String(200), nullable=False)

    # condition 将来传递参数 来获取数据
    def GetProjectByCondition(self, condition={}):
        project_list = Project.session.query(Project).order_by(Project.id.desc()).all()
        return project_list

    #更新project status
    def updateProjectStatus(self, id, status):
        return Project.Q.filter(Project.id == id).update({Project.status: status}, synchronize_session='fetch')

    #添加project 或者修改
    def addProject(self, params, id=0):
        if id == 0:
            new_project = Project(name=params['name'], status=params['status'], checkcode=params['checkcode'],
                                  checkemail=params['checkemail'],path=params['path'], git_path=params['git_path'])
            Project.session.add(new_project)
            Project.session.commit()
            return 1
        else:
            return Project.Q.filter(Project.id==id).update(params, synchronize_session='fetch')

    #获取项目信息
    def getProjectInfo(self, id):

        return Project.Q.filter(Project.id == id).limit(1).all()