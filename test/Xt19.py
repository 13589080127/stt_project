# -*- coding: utf-8 -*-

#函数和变量

def cheese_and_crackers(cheese_count, box_of_crackers):
	print "Yo have %d cheeses?" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




#练习
# def add(a, b):
#     print("The first number is: %d" % a)
#     print("The other number is: %d" % b)
#     print("Now I'm going to add the two number: %d" % (a+b))
# print("My first try:")
# add(10, 20)
# print("Again:")
# add(10-2, 20+3)
# print("the third time:")
# aa = 17
# bb = 9
# add(aa, bb)
# print("Fourth time:")
# add(aa+3, bb/3)
