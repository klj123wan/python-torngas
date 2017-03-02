create database sync;

use sync;
DROP TABLE IF EXISTS `codedeploy`;
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
