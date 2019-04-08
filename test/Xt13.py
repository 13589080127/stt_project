# -*- coding: utf-8 -*-

#参数、解包和变量

#from sys import argv            #sys.argv[]用来获取命令行参数

#script, first, second, third  = argv     
#报错如下：ValueError: need more than 1 value to unpack
#解决方案如下：python Xt13.py script, first, second
#解决原因：


#print "The script is a called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third


#father, mother, baby1, baby2, baby3 = argv     #执行时输入的变量为4个，执行成功；5个时，执行失败，查看网上执行结果一致

#print "FJY is:", father
#print "STT is:", mother
#print "one is:", baby1
#print "two is:", baby2
#print "three is:", baby3




#网上的习题答案：raw_input和argv共用
from sys import argv

script, name, age = argv

print "The script is called:", script          #python Xt13.py 1 2        实际中并没有这一句
print "Your name is:", name
print "Your age is:", age

print "Your height is:",
height = raw_input()
print "Your weight is:",
weight = raw_input()
