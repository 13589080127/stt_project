# -*- coding: utf-8

# 提问

#print "How old are you?"
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weighe?",
#weight = raw_input()
#
#print "3+2=", 3+2
#print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)











print "Please input a num:"
j = raw_input()
k = bool(j)
#print k
#print type(k)
if k:    #if j != ''     if j != ''      if 后面必须是bool类型
	print j
else:
	print "this var is not values"
#给我一个变量，如果这个变量有值的话，打印变量的内容；如果没有值的话，打印“这个变量没有值”