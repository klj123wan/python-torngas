项目介绍
	
	后端：python的torngas框架
	前端：基于bootstrap的admintle框架编写
	

项目目录介绍

	参考文件 TORNGASREADME.md

项目配置

	主要配置在 /demo/settings/setting.py 文件中
	包含: mysql 静态文件位置 模板位置 日志等
	
python需要安装扩展库

	mysql-python
	tornado
	torngas
	SQLAlchemy
	requests
	redis


RSYNC 安装

    参考 
        http://sookk8.blog.51cto.com/455855/328076/
        http://www.cnblogs.com/itech/archive/2009/08/10/1542945.html
        
    
    wget https://rsync.samba.org/ftp/rsync/rsync-3.1.2.tar.gz
    tar -zxvf rsync-3.1.2.tar.gz
    cd rsync-3.1.2
    ./configure --prefix=/usr/local/rsync
    make
    make install
    
RSYNC 配置
    
    目标机 --- 服务端
        启动服务 /usr/bin/rsync --daemon
        服务端配置 vim /etc/rsyncd.conf
        uid = nobody    
        gid = nobody
        use chroot = no
        max connections = 4
        stirict modes = yes
        port = 873
        
        [backup]  # 同步路径配置
        
        path = /data/www/
        comment = This is a test
        ignore errors
        read only = false
        list = no
        #hosts allow = 114.255.234.50 # 访问机器允许
        hosts allow = *
        hosts deny = 0.0.0.0/0
        auth users = konglj   #用户配置
        secrets file =/etc/rsyncd.pw
        pid file = /var/run/rsyncd.pid
        lock file = /var/run/rsync.lock
        log file = /var/log/rsyncd.log
        
        密码配置 vim /etc/rsyncd.pw
        用户名：密码
        即 konglj:123456
        
        
    客户端 只需要安装rsync即可 
    rsync -av www.torngas.com/* konglj@0.0.0.0::backup/www.torngas.com    
    
代码发布系统参考

    http://www.cnblogs.com/itcomputer/p/4884688.html
    

CRONDTAB

    #上线代码
    * * * * * /user/bin/python -m demo.cron.deploy
    #回滚代码
    * * * * * /user/bin/python -m demo.cron.rollback