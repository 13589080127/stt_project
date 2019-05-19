# -*- coding: utf-8 -*-

#那是什么

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:     #只是代替字符，占位？
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#附加练习
#while True:
#    for i in ["/","-","|","\\","|"]:
#	    print "%s\r" % i,
		
		
#\r回车符，backspace掉\r前的所有字符
#\t水平制表符，相当于tab键，空4格
#\n换行          
#\b退格符，回退一格
#\a响铃符，执行时格式无变化，但是会有声音提示



#将转义序列和格式化字符串组合到一起，创建一种更复杂的格式
from sys import argv
script, one = argv

print "hello, \n%r" % one
