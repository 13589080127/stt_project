# -*- coding: utf-8 -*-

#读取文件

from sys import argv

script, filename = argv

#yyy = open('Xt9.py')       #open是一个打开文件的方法，后面跟得是字符串，所以括号里面要带引号。同级别目录无需写具体路径，不同级别文件，需在引号中，注明具体路径

txt = open(filename)           #打开通过解包得到的文件，赋值给txt
#open(name[, mode[, buffering]])

#print "Here's your file %r:" % 'Xt9.py'
#print yyy.read()


#读其他文件
laogong = open('F:\zcsmart\JZSY\jzsy-common\src\main\java\com\zcsmart\jzsy\code\AbstractCode.java')
print 'F:\zcsmart\JZSY\jzsy-common\src\main\java\com\zcsmart\jzsy\code\AbstractCode.java'

laogong.close()      #ValueError: I/O operation on closed file   input入/output出 不能在关闭的文件中执行I/O操作
print laogong.read()
#laogong.close()       

print "Here's your file %r:" % filename
print txt.read()     #读这个文件的内容，并打印出来
#read方法只有一个参数，如输入多个参数read（3,3），返回：TypeError: read() takes at most 1 argument (2 given)
  #read（3）即读取被读取文件的前3个字符；read（），读取被读取文件的全部内容

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()



