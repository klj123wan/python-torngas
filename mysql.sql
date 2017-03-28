create database sync;

use sync;
DROP TABLE IF EXISTS `project`;
CREATE TABLE `project` (
    `id` tinyint(4) NOT NULL auto_increment,
    `name` varchar(32) NOT NULL,
    `status` tinyint(1) NOT NULL default '1',
    `checkcode` tinyint(1) unsigned NOT NULL default '0' COMMENT '代码是否需要审核',
    `checkemail` varchar(50) default NULL,
    `path` varchar(30) default NULL,
    `git_path` varchar(200) not null default '' comment 'git仓库路径',
    PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT "项目列表";

use sync;
DROP TABLE IF EXISTS `deploy_log`;
CREATE TABLE `deploy_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL default 0 comment '用户id',
  `username` varchar(64) NOT NULL default '' comment '用户名称',
  `description` varchar(1024) NOT NULL default '' comment '上线原因' ,
  `project` varchar(32) NOT NULL default '' comment '线上目录',
  `files` varchar(4096) NOT NULL default '' comment '上线文件',
  `userip` varchar(15) NOT NULL default '' comment '用户ip',
  `created` int(11) NOT NULL default 0 comment '创建时间',
  `feedback` int(11) NOT NULL default 0 comment '是否审核',
  `status` tinyint(4) NOT NULL COMMENT '-1 is abandoned\\n0 is unproccess\\n1 is processed\\n2 is error -> from server\\n3 is success -> everything is done\\n',
  `log_from_server` varchar(1024) NOT NULL,
  `pid` tinyint(4) unsigned NOT NULL DEFAULT '0' COMMENT '项目编号',
  `email` varchar(32) NOT NULL DEFAULT '' COMMENT '提交代码用户的email',
  `tagid` int(11) not null default 0 comment 'git tag版本',
  PRIMARY KEY (`id`),
  KEY `pid` (`pid`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 comment "记录日志";