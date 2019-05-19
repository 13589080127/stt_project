# -*- coding: utf-8 -*-

#函数和文件

from sys import argv

script, input_file = argv

def print_all(f):   #新建print_all函数
	print f.read()  #定义print f.read()为函数代码，读f这个脚本并打印出来

def rewind(f):   #新建rewind函数
	f.seek(0)    #定义f.seek(0)为函数代码，seek() 方法用于移动文件读取指针到指定位置
#seek语法：  fileObject.seek(offset[, whence])
	#offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    #whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
	#如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1
	
		
def print_a_line(line_count,f):     #新建print_a_line函数
	print line_count, f.readline()  #定义print (line_count , f.readline())为函数代码
	
current_file = open(input_file)   #打开input_file文件，并赋值给current_file

print "First let's print the whole file:\n"

print_all(current_file)    #????????

print "Now let's rewind, kind of like a tape."

rewind(current_file)   #定位当前位置

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)  #打印第一行    调用print_a_line函数（line_count = current_line = 1，f.readline = current_file文件名）

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)






#+=操作符的作用        直接python 中可操作,aaa.py脚本

#英语里边 “it is” 可以写成 “it’s”，”you are” 可以写成 “you’re”，这叫做简写
#用法一：相加，然后返回值给前一个变量
#a=1
#b=2
#a+=b
#a
#3
#用法二：字符串连接
#a='1'
#b='2'
#a+=b
#a
#'12'