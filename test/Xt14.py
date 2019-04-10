# -*- coding: utf-8 -*-

#提示和传递

from sys import argv      

script, user_name, password = argv            #执行时，为1个参数  python Xt14.py 1    script 脚本
com = '>'

print "Hi %s, I'm the %s script password is %s." % (user_name, script, password)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(com)

print "Where do you live %s?" % user_name
lives = raw_input(com)

print "What kind of computer do you have?"
computer = raw_input(com)

print """
Alright, so you said %r about liking me.
You have in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
