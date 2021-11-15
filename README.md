# OSMChina-TileLog
TileLog Analysor for OSMC

---

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
