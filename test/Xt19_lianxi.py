# -*- coding: utf-8 -*-

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




#7种方法调用
def  auto_sum(sub1,sub2):
    sum = sub1 + sub2
    print("打印出参数1：{sub1}")
    print("打印出参数2：{sub2}")
    print("两个参数的和是多少：{sum}")
    print("--------------------")
    return sum

print("直接写参数，调用该函数方法1：")
auto_sum(10,20)


print("使用两个变量参数，调用函数方法2：")
add1 = 300.55
add2 = 299.99
auto_sum(add1,add2)


print("使用表达式，调用函数方法3：")
auto_sum(float(12.22*35),960/40)

print("人工输入两个参数值，调用函数方法4：")
a = int(input("请输入第一个加数1："))
b = int(input("请输入第二个加数2："))
auto_sum(a,b)
#不要随意变更变量a和b的类型，影响使用a和b的
print("使用全局变量的两个参数值并计算后，调用函数方法5：")
auto_sum(a * 23, b % 3)

print("其中一个参数人工输入，调用函数方法6：")
one = int(input("请输入要计算的数字："))
auto_sum(one,int(input("请输入第二个要计算的数字：")))

print("给一个变量赋值为函数，调用函数方法7：")
a = auto_sum(22,88)
print(f"a的值是多少：{a}")




#多种方法调用

def apple(a,b):

    c1 = 100 - a - b

    print "There are 100 apples."

    print "If you give %d apples to your father." % a

    print "And give %d apples to your monther." % b

    print "Finally, you will have %d apples.\n" % c

print "case1:"

apple(10,20)

print "case2:"

a = 10

b = 50

apple(a,b)

print "case3:"

a = 50

apple(a,50)

print "case4:"

b = 30

apple(20,b)

print "case5:"

a = int(raw_input("a = "))

b =  20

apple(a,b)

a = int(raw_input("case6:\na = "))

b = int(raw_input("b = "))

apple(a,b)

print "case7:"

a = 10

b = int(raw_input("b = "))

apple(a,b)

a = int(raw_input("case8:\na = "))

b = int(raw_input("b = "))

apple(a + 10,b)

a = int(raw_input("case9:\na = "))

b = int(raw_input("b = "))

apple(a, b + 20)

a = int(raw_input("case10:\na = "))

b = int(raw_input("b = "))

apple( a + 10, b + 20)