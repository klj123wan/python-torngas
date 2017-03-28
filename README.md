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


RSYNC 安装

    参考 http://sookk8.blog.51cto.com/455855/328076/
    
    wget https://rsync.samba.org/ftp/rsync/rsync-3.1.2.tar.gz
    tar -zxvf rsync-3.1.2.tar.gz
    cd rsync-3.1.2
    ./configure --prefix=/usr/local/rsync
    make
    make install
    
代码发布系统参考

    http://www.cnblogs.com/itcomputer/p/4884688.html
    


