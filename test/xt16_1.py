# -*- coding: utf-8 -*-

# 读写文件

from sys import  argv    #从sys代码库中导入argv这个方法

script, filename = argv   #将argv这个方法进行解包，解包得到script, filename两个变量

#print "We're going to erase %r." % filename      #####打开一个存在的文件      #打印“”， % filename 进行替换%r
#print "If you don't want that, hit CTRL-C (^C)."    #####hit CTRL-C (^C)在这里只是做字符串？           #print""
#print "If you do want that, hit RETURN."    #print“”
#
#raw_input("?")   #获取控制台，光标放在终端上
#
#print "Opening the file..."     #print“”
#target = open(filename, 'r')   #打开XXX文件，并将值赋予target这个变量
#有+和无+：
#现阶段对文档的操作主要常见的有，w+、r+、a+
#write：无+，只能对文档进行写操作；有+，即可对文档写操作，也可进行读操作
#read：无+，target.append,  AttributeError: 'file' object has no attribute 'append'
           #target.read,  可操作
		   #target.write,  IOError: File not open for writing
		   
#只对文件进行读操作，如进行写操作：IOError: File not open for writing；


      #有+，target.append,  AttributeError: 'file' object has no attribute 'append'
	        #target.read,  可操作
		    #target.write,  TypeError: function takes exactly 1 argument (0 given)(！！！无需新建对象)
	  
#append：无+，target.append,  AttributeError: 'file' object has no attribute 'append'（attributeError:“file”对象没有“append”属性）；
              #target.read,  IOError: File not open for reading
              #target.write,  TypeError: function takes exactly 1 argument (0 given)
			  
        #有+，target.append,  AttributeError: 'file' object has no attribute 'append'
              #target.read,  可操作
			  #target.write,  TypeError: function takes exactly 1 argument (0 given)
			  
			  
#print "Truncating the file. Goodbye!"     #print“”
#target.truncate()     #truncate清除target这个文件

#rint "Now I'm going to ask you for three lines."     #print“”
#
#ine1 = raw_input("line 1: ")   #获取控制台，光标放在终端上
#ine2 = raw_input("line 2: ")   #获取控制台，光标放在终端上
#ine3 = raw_input("line 3: ")   #获取控制台，光标放在终端上
#
#rint "I'm going to write these to the file."   #print“”

#target.write(line1)  #写target文件的第一行？
#target.write("\n")   #为什么\n不在line1后面
#target.write(line2)
#target.write("\n")   #转移符只在字符串中有效，不带引号的\n会被视作变量
#target.write(line3)
#target.write("\n")
#练习：试着用一个 target.write() 将 line1, line2, line3 打 印出来，你可以使用字符串、格式化字符、以及转义字符
#target.write(line1+"\n"+line2+"\n"+line3+"\n")     #转移符只在字符串中有效，不带引号的\n会被视作变量arget
#haha = open(filename, 'a+')
#haha.write("ddd")    #w+写入文件后，会把原文件内容，覆盖掉    a+文档末尾追加

www = open(filename,"r")
d = www.read()

newFile = open(filename,"w")
print "all content:", d
q = d + "ac"
print "new content:", q
newFile.write(q)
newFile.close()


#print "And finally, we close it."
#target.close()   #target是target = open(filename, 'w') 赋值得到的，那filename是否需要关闭
#
#haha.close()
