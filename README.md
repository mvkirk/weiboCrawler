# weiboCrawler
## database.py
database.py内定义了数据库接口，数据表默认定义在服务器115.159.127.117上，用户名为crawler,数据库名为weibo。内含两个数据表，use表和relation表。

  CREATE TABLE `user` (
     `uid` varchar(20) NOT NULL,
     `containerId` varchar(20) NOT NULL,
     `name` varchar(50) NOT NULL,
     `gender` varchar(5) NOT NULL,
     `description` mediumtext,
     `nativePlace` varchar(10) DEFAULT NULL,
     PRIMARY KEY (`uid`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

  CREATE TABLE `relation` (
    `fansId` varchar(20) NOT NULL DEFAULT '',
    `followerId` varchar(20) NOT NULL DEFAULT '',
    PRIMARY KEY (`fansId`,`followerId`),
    KEY `fansIdIndex` (`fansId`),
    KEY `followerIdIndex` (`followerId`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8

分别保存用户信息和用户之间的关注关系。
## follower.py
follower.py内封装了对于指定用户爬取其关注的用户的方法。
## opener.py
opener.py内独立封装了一些防反爬虫的头信息。
## test.py
test.py内封装了测试代理连通性的方法。
## work.py
work.py内是整个程序的入口，定义了bfs的爬虫方案，并实时输出log到屏幕以及userGet.log文件内。
