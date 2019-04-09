# -*- coding: utf-8 -*-

#读取文件

from sys import argv

script, filename = argv

txt = open(filename)
#open(name[, mode[, buffering]])

print "Here's your file %r:" % filename
print txt.read()  #为空，报错；为filename报必须是整数，；为1，有#号出现，且报错

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
