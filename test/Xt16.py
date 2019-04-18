# -*- coding: utf-8 -*-

# 读写文件


#= = 和true、false如何使用 
#
#习题4，常见问题回答，print时词语间的空格……
#
#习题5，常见问题回答，浮点数四舍五入，round（1.773）



from sys import  argv    #从sys代码库中导入argv这个方法

script, filename = argv   #将argv这个方法进行解包，解包得到script, filename两个变量

print "We're going to erase %r." % filename      #####打开一个存在的文件      #打印“”， % filename 进行替换%r
print "If you don't want that, hit CTRL-C (^C)."    #####hit CTRL-C (^C)在这里只是做字符串？           #print""
print "If you do want that, hit RETURN."    #print“”

raw_input("?")   #获取控制台，光标放在终端上

print "Opening the file..."     #print“”
target = open(filename, 'w+')    ####'w' 的作用？？书侯敏有解释，w必带吗？     #打开XXX文件，并将值赋予target这个变量
#有+和无+


print "Truncating the file. Goodbye!"     #print“”
#target.truncate()     #truncate清除target这个文件

print "Now I'm going to ask you for three lines."     #print“”

line1 = raw_input("line 1: ")   #获取控制台，光标放在终端上
line2 = raw_input("line 2: ")   #获取控制台，光标放在终端上
line3 = raw_input("line 3: ")   #获取控制台，光标放在终端上

print "I'm going to write these to the file."   #print“”

#target.write(line1)  #写target文件的第一行？
#target.write("\n")   #为什么\n不在line1后面
#target.write(line2)
#target.write("\n")   #转移符只在字符串中有效，不带引号的\n会被视作变量
#target.write(line3)
#target.write("\n")
#练习：试着用一个 target.write() 将 line1, line2, line3 打 印出来，你可以使用字符串、格式化字符、以及转义字符
#target.write(line1+"\n"+line2+"\n"+line3+"\n")  
target.read()

print "And finally, we close it."
target.close()   #target是target = open(filename, 'w') 赋值得到的，那filename是否需要关闭
