# -*- coding: utf-8 -*-

#字符串和文体

x = "There are %d types of people." % 10     #变量    这里有十个人    %10替换里面的%d 
binary = "binary"   #变量
do_not = "don't"    #变量
y = "Those who know %s and those who %s." % (binary, do_not)  
#变量  这些人谁知道binary，谁知道do_not  ，，binary, do_not以先后顺序进行替换%s 

print x
print y

print "I said: %r." % x 
print "I also said: ‘%s’." % y

hilarious = False  #变量   滑稽的
joke_evaluation = "Isn't that joke so funny?! %r"   #变量    笑话_评估

print joke_evaluation % hilarious  #打印：% hilarious替换%r

w = "This is the left side of..."   #变量
e = "a string with a right side."   #变量

print w + e