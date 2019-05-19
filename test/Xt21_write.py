# -*-  coding: utf-8 -*-

def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def divide(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b
	
#方法一：

age = add(20, 4)
time = subtract(40, 6)
hello = divide(1000, 10)
haha = add(1000, 23)          #感觉打印结果有问题，adding等打印两次，Xt21.py中，def位置未打印。。。。且sum值不对
sum = subtract(time,add(age,subtract(40, 6)))

print sum


#方法二：
