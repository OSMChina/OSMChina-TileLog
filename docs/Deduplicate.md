# 去重

目前初步考虑的是用最简单的时间码url内容字节等逐一匹配的方式，挨个对比，完全一样就是一条

当然还是应该给一些参数的，比如“忽视时间”“忽视字节数目”“忽视referer”等。