# -*- coding: utf-8 -*-

f = open('Xt1.py', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # 移动到文件的第六个字节

f.read(1)

f.seek(-3, 2)  # 移动到文件倒数第三个字节

f.read(1)






#文件 runoob.txt 的内容如下：
www.runoob.com
www.runoob.com
www.runoob.com
www.runoob.com
www.runoob.com


#循环读取文件的内容：

# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
 
line = fo.readline()
print ("读取的数据为: %s" % (line))
 
# 重新设置文件读取指针到开头
fo.seek(0, 0)
line = fo.readline()
print ("读取的数据为: %s" % (line))
 
 
# 关闭文件
fo.close()




#以上实例输出结果为：

文件名为:  runoob.txt
读取的数据为: 1:www.runoob.com

读取的数据为: 1:www.runoob.com