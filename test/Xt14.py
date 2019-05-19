# -*- coding: utf-8 -*-

#提示和传递

from sys import argv      

script, user_name, password = argv            #执行时，为1个参数  python Xt14.py 1    script 脚本
#computer = '>'     #和无变量命名，直接提示一样。提示符设置为变量 prompt，这样我们就不需要在每次用到 raw_input 时重复输入提示用户的字符了

print "Hi %s, I'm the %s script password is %s." % (user_name, script, password)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(">")

print "Where do you live %s?" % user_name
lives = raw_input(computer)

print "What kind of computer do you have?"
computer = raw_input(computer)

print """
Alright, so you said %r about liking me.
You have in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
