# -*- coding: utf-8 -*-

#更多的变量和打印

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

transfer_height = 2.54 * my_height # cm
transfer_weight = 0.45359237 * my_weight # kg



print "Let's talk about %s." % my_name    #这里其实是以后面同%s相同结构的替换
print "He's %d inches tall." % transfer_height
print "He's %d pounds heavy." % transfer_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If i add %d , %d, and %d i get %d." % (my_age, transfer_height, transfer_weight, my_age + transfer_height + transfer_weight)
