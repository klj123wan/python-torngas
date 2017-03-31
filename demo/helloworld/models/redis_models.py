# -*-coding=utf8-*-
# your models module write here

from torngas import settings
from torngas.cache.backends.base import *
from torngas.cache.backends.rediscache import *
redisModel = RedisCache(settings.CACHES.default_redis['LOCATION'], settings.CACHES.default_redis['OPTIONS'])
redisClient  = RedisClient(settings.CACHES.default_redis['LOCATION'], settings.CACHES.default_redis['OPTIONS'])

class Redis():

    #向上线队列中推送数据
    def pushDeploy(self, id):
        return redisClient._client.lpush(self.getDeployKey(), id)

    #上线队列的key
    def getDeployKey(self):
        return 'rsync:deploy'

    #从上线队列取出一条数据
    def popDelpoy(self):
        return redisClient._client.rpop(self.getDeployKey())

    def lenDeploy(self):
        return redisClient._client.llen(self.getDeployKey())

    # 向回滚队列中推送数据
    def pushRollBack(self, id):
        return redisClient._client.lpush(self.getDeployKey(), id)

    # 回滚队列的key
    def getRollBaclKey(self):
        return 'rsync:rollback'

    # 从回滚队列取出一条数据
    def popRollBack(self):
        return redisClient._client.rpop(self.getDeployKey())

    #获取回滚队列长度
    def lenRollBack(self):
        return redisClient._client.llen(self.getDeployKey())

