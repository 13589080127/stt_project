# -*-  coding: utf-8 -*-

def add(a, b):
    print "adding %d + %d" % (a, b)     #为什么要用%d
    return a + b

def subtract(a, b):
    print "subtracting %d - %d" % (a, b)     #为什么执行结果先返回了subtracting，后返回add
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b

age = 1
height = 1
weight = 4
iq = 4

what = 100

temp3 = subtract(what, age)
temp2 = add(temp3, height)
temp1 = divide(temp2, weight)
temp = multiply(temp1, iq)

print "answer is %d " % temp