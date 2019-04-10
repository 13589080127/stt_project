# -*- coding: utf-8 -*-

#读取文件

from sys import argv

script, filename = argv

txt = open(filename)           #打开通过解包得到的文件，赋值给txt
#open(name[, mode[, buffering]])

print "Here's your file %r:" % filename
print txt.read()     #读这个文件的内容，并打印出来
#read方法只有一个参数，如输入多个参数read（3,3），返回：TypeError: read() takes at most 1 argument (2 given)
  #read（3）即读取被读取文件的前3个字符；read（），读取被读取文件的全部内容

print "Type the filename again:"
#file_again = raw_input(">")
#
#txt_again = open(file_again)
#
#print txt_again.read()
