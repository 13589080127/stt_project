# -*- coding: utf-8 -*-

#更多文件操作   将一个文件内容，写入到另一个文件  from_file写入到to_file

#其实例题的意思就是一开始先得到两个文件名作为参数，然后打开已经编辑好的file，并且file.read()。
#再len(file)这个文件的大小。然后检查另一份file是否存在–exists(file)。这个函数返回bool类型。
#最后打开这份文件并且进行file.write()，内容就是第一份file中的数据。别忘记了file.close()，在上一章中介绍close()就类似保存退出。


from sys import argv   #从sys代码库中导入argv这个功能
from os.path import exists   #检查文件是否存在    从os.path(系统.路径)导入存在   exists将文件名字符串作为参 数，如果文件存在的话，它将返回 True，否则将返回 False

#os.path模块，主要用于文件属性的获取，
#os.path.exists(path)   如果path存在，返回True；如果path不存在，返回False。

script, from_file, to_file = argv   #将argv这个方法进行解包，解包得到script, from_file, to_file三个变量

print "Copying from %s to %s" % (from_file, to_file)   #打印“”， % from_file, to_file 依次进行替换%s

#we could do these two on one line too, how?
in_file = open(from_file)   #打开from_file文件，赋值给in_file
indata = in_file.read()   #读in_file，并赋值给indata    #读操作怎么赋值？独到的内容进行赋值？

print "The input file is %d bytes long" % len(indata)    #把indata的长度带入到%d  文件的长度，空格也算一个字符


##Python len() 方法返回对象（字符、列表、元组等）长度或项目个数
#用法一：len( s )   --s对像

#用法二：返回字符串长度
#str = "runoob"
#len(str)   #返回长度为6   一般来说，一个字符一个长度

#用法三：返回元素个数
#l = [1,2,3,4,5]   []集合，1,2,3,4,5元素    集合，即容器，装了哪些东西。又叫列表list,
#len(l)   #返回个数为5


print "Dose the output file exist? %r" % exists (to_file)  #to_file文件名字符串作为exists方法的参数，True或False,替代到%r

#print拼接，后面跟字符串“”、init类型5+2，变量=、bool类型（exists方法返回）
#exists (to_file) 是一个方法，所以会先执行
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()



#把习题尽可能的写短一些
from sys import argv 
from os.path import exists
script, from_file, to_file = argv
print "The input file is %d bytes long" % len(open(from_file).read())
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()
in_file.close()
