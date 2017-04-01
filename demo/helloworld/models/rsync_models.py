# -*-coding=utf8-*-
# your models module write here

from torngas.db.dbalchemy import Model
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
import time
import datetime


class BaseModel(Model):
    __abstract__ = True
    __connection_name__ = 'default'

    id = Column(Integer, primary_key=True, nullable=False)

class Rsync(BaseModel):
    __tablename__ = 'deploy_log'

    id = Column(Integer, primary_key=True, nullable=False)
    uid = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    username = Column(String(64), nullable=False)
    description = Column(String(1024), nullable=False)
    project = Column(String(32), nullable=False)
    files = Column(String(20480), nullable=False)
    userip = Column(String(15), nullable=False)
    created = Column(Integer, nullable=False)
    feedback = Column(Integer, nullable=True)
    log_from_server = Column(String(1024), nullable=True)
    pid = Column(Integer, nullable=False)
    email = Column(String(64), nullable=False)
    tagid = Column(Integer, nullable=False)

    # condition 将来传递参数 来获取数据
    def GetProjectByCondition(self, condition={}):
        #project_list = Project.session.query(Project).order_by(Project.id.desc()).all()
        return ''

    # 更新project status
    def updateRsyncStatus(self, id, status):
        return Rsync.Q.filter(Rsync.id == id).update({Rsync.status: status}, synchronize_session='fetch')


    # 添加project 或者修改
    def addRsync(self, params):
        new_deploy = Rsync(uid=params['uid'], status=params['status'],username=params['username'], description=params['description'],
                           project=params['project'], files=params['files'], pid=params['pid'], email=params['email'],
                           userip=params['userip'],created=time.time(),feedback=0,log_from_server='',tagid=params['tagid'])
        Rsync.session.add(new_deploy)
        Rsync.session.commit()
        return 1

    # 获取项目信息
    def getRsyncInfo(self, id):
        return Rsync.Q.filter(Rsync.id == id).limit(1).all()

    # 获取所有状态正常的项目
    def getNormalProjects(self):
        #return Project.Q.filter(Project.status == 1).all()
        return 1

    def getNotPublishRsync(self):
        return Rsync.Q.filter(Rsync.status==0).order_by(Rsync.id.desc()).all()

    #获取最后一条项目更新的记录
    def getLastRsync(self, pid):
        return Rsync.Q.filter(Rsync.pid == pid).order_by(Rsync.id.desc()).limit(1).all()

    def getPublishRsync(self, params):
        where = "status != '0' "
        if params['project'] != 0:
            where += " and pid= '" + str(params['project']) + "'"
        if params['sdate'] != '':
            sdate = time.mktime(time.strptime(params['sdate'], "%Y-%m-%d"))
            where += " and created >= '" + str(int(sdate)) + "'"
        if params['edate'] != '':
            edate = time.mktime(time.strptime(params['edate'], "%Y-%m-%d"))
            where += " and created <= '" + str(int(edate)) + "'"
        if params['uname'] != '':
            where += " and username like '%" + params['uname'] + "%'"
        return Rsync.Q.filter(where).order_by(Rsync.id.desc()).limit(1000).all()
