# -*- coding: utf-8 -*-
#更多练习

print "Lte's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'   #转译符

poem = """
\tThe lovely world     #水平制表符，缩进4格
with logic so firmly planted
cannot discern \n the needs of love     #换行
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.    #换行、缩进四格、四格
"""

print "----------"
print poem
print "----------"


five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)  #这一行的作用是什么？变量？解包？

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)