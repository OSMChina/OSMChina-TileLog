# Parse

其实是有现成的商业服务可以用的，如“日志易”这种东西，号称是：

> 支持各种类型的日志：任何基于文本类型的日志，无论来自服务器或是客户端，例如Apache、Java、PHP、Tomcat、MySQL、syslog-ng、rsyslog、nxlog、路由器等网络设备的日志，都可以上传到日志易

Reference：https://www.rizhiyi.com/assets/ebooks/bannerbook.pdf

但是不推荐高度依赖互联网服务，顶多写一个Parser对它的输出转换成可输入本系统的工具

----

下面是选型过程（也是同类产品参考，建议后期开awesome-apache-log）


## 解析

（后期应分离Apache后端和其他后端，如官方后端）

首先，进行技术选型

在Github上有不少apachelog的解析库
但是并非所有都是有价值的

不太想尝试的有：
golang https://github.com/Songmu/axslogparser
ruby https://github.com/weppos/apachelogregex
php https://github.com/mvar/apache2-log-parser
java https://github.com/nielsbasjes/logparser

用py写的有：
https://github.com/lethain/apache-log-parser
https://github.com/mthbernardes/ARTLAS
这两个做备选

很出名但是不是py的：
https://github.com/wvanbergen/request-log-analyzer  这个有2.2k 星星，应该可以生产用
https://github.com/alvinj/ScalaApacheAccessLogParser scala

打算首选https://github.com/amandasaurus/apache-log-parser

次选ARTLAS

---

国内CSDN和博客园上有这些个人写的小轮子，但是不是很想用
https://blog.csdn.net/weixin_45843450/article/details/106418701
https://www.jb51.net/article/61395.htm
https://blog.csdn.net/a_guai_/article/details/105254734
https://www.jianshu.com/p/f866f2ed73ce
http://www.cocoachina.com/articles/64330

有一个用alp的
https://blog.csdn.net/weixin_45427650/article/details/105368149
