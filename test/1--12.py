#-*- coding: utf-8 -*-

#习题1——12，练习题

#1、计算25除以5（两种方式，浮点和整数）

print ("25 / 5 = ",25 / 2)
print ("25 / 5 = ",25.0 / 2.0)

#2、给你三个变量，怎么样将三个变量拼接以后成为新的变量并打印出来

father = "haohao"
mother = "tiantian"
baby = "haobao"

we = father + mother + baby
print (we, "are family" )



print "%s, %s, %s" % (father, mother, baby)    #替换符必须在字符串里，才能替换

#3、怎么在代码里使用转译

print ("1, \n2, \n\t3,       \b4")

#4、写出一个简单的for循环
 
 
for suibian in range(0,6):
	print suibian

 
#无限循环
#while True:
	#for suibian in range(0,1001):
		#print suibian
		
#给你一个变量，把他的类型打印出来，   ！！！！！并且判断类型是不是bool类型（此操作未执行）
print "his gener?"
haohao = raw_input()
#print haohao
#type = int(raw_input())
print type(haohao)



renyao = bool(haohao)
if renyao:
	print haohao
	
else:
	print "haohao grner is null"





#haohao = raw_input("his gener?")

 