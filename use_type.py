#coding=utf-8
#Python2中默认是ASCII码，一般会加入以utf-8编程
a = '编码'                       # a是utf-8类型
b = a.decode('utf-8')       # b是Unicode类型
c = b.encode('gbk')        #c是gbk类型
d = c.decode('gbk').encode('utf-8')   #先将c转换成Unicode，再转成utf-8
print a ,b,c,d
print type(a),type(b),type(c),type(d)
