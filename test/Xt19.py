# -*- coding: utf-8 -*-

#函数和变量

def cheese_and_crackers(cheese_count, boxes_of_crackers):    
# 声明了cheese_and_crackers这个函数,该函数有两个参数，分别是cheese_count和boxes_of_crackers.
# 函数其实就是个print的集合
	print "Yo have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"      #打印“Get a blanket.”并空出一行
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)      # 调用了这个函数，带入两个参数（20, 30）

print "Or, we can use variables from our script:"
amount_of_cheese = 10    # 声明并定义了两个变量
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)    # 将之前定义的两个变量调用到函数中

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)      # 引入的实参是一个运算式

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)    # 引入的实参是个变量运算
