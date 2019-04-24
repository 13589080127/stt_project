# -*- coding: utf-8 -*-

#命名、变量、代码和函数

#“‘运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思”

#注意事项如下：
#1. 函数定义是以  def 开始的
#2. 函数名称是以字符和下划线  _ 组成的
#3. 函数名称紧跟着括号  ( 
#4. 括号里可以包含参数，多个参数要用逗号隔开
#5. 不能使用重复的参数名
#6. 紧跟着参数的是括号和冒号  ): 
#7. 紧跟着函数定义的代码使用了 4 个空格的缩进 ( indent )
#8. 函数结束的位置取消了缩进 (“dedent”)


#this one is like your scripts with argv
def print_two(*args):    #定义print_two这个函数，需要的参数为*args     
#*args指它的功能是告诉 python 让它把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。   args列表？？？？？？

	arg1, arg2 = args    #将args进行解包，得到……
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless,we can just do this
def print_two_again(arg1, arg2)
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#this just takes one argument
def print_none():
	print "I got nothin'."
	
print_two("Zed","Shaw")
print_two_again("Zed“，"Shaw")
print_one("First!")
print_none()
