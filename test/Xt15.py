# -*- coding: utf-8 -*-

#读取文件

from sys import argv   #从sys代码库中导入argv这个方法

script, filename = argv   #将argv这个方法进行解包，解包得到script, filename两个变量


txt = open(filename)   #打开通过解包得到的文件，赋值给txt
print "Here's your file %r:" % filename   #打印“”， % filename 进行替换%r
print txt.read()     #读这个文件的内容，并打印出来      readline()，读取文件中的一行

#read方法只有一个参数，如输入多个参数read（3,3），返回：TypeError: read() takes at most 1 argument (2 given)
#read（3）即读取被读取文件的第3个字符之前的；read（），读取被读取文件的全部内容
  
  
  
#练习，打开同路径文件
#yyy = open('Xt9.py')       #open是一个打开文件的方法，后面跟得是字符串，所以括号里面要带引号。同级别目录无需写具体路径，不同级别文件，需在引号中，注明具体路径
#print "Here's your file %r:" % 'Xt9.py'
#print yyy.read()



#读其他路径文件
#laogong = open('F:\zcsmart\JZSY\jzsy-common\src\main\java\com\zcsmart\jzsy\code\AbstractCode.java')
#print 'F:\zcsmart\JZSY\jzsy-common\src\main\java\com\zcsmart\jzsy\code\AbstractCode.java'

#laogong.close()   
#如果在read之前，将文件关闭，报错如下：
#ValueError: I/O operation on closed file   input入/output出 不能在关闭的文件中执行I/O操作
#print laogong.read()
#laogong.close()   #注意：对文件操作以后，如写操作、读操作等，需要对文件进行关闭操作，以防资源占用      



print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()