# -*-  coding: utf-8 -*-

#函数可以返回某些东西

def add(a, b):        #定义一个函数，下同，函数的运算分别加、减、乘和除
	print  "adding %d +  %d" % (a, b)
	return a + b      #函数返回a+b的值，下同，对应各自的运算

def subtract(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"   #print"用下面的值做一些计算“      使用下面四个函数，并赋值给左侧
age = add(30, 5)
height = subtract(78, 4)   #加减，是规定以前一个减去后一个？
weight = multiply(90, 2) 
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for the extra credit, type it in anyway. 
print "Here is a puzzle."  #这里有个智力游戏

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))     
#嵌套函数，4个函数3层嵌套,其中divide的结果做multiply的参数，mutiply的结果又做subtract的参数，subtract的结果又做add的参数，所以是3层嵌套

#这个公式稍稍有点复杂，应该从内往外开始读
#1. 上面分别通过函数计算得到了age、height、weight、iq的值
#2. 然后把这些值套用到函数中得到下面这样一个数学表达式
#3. what = (35+(74-(180*(50/2))))= 35 + 74 - 180 * 50 / 2
#4. 得到的结果就是-4391

print "That's becomes: ", what, "Can you do it by hand?"    #两个字符串之间加了变量
