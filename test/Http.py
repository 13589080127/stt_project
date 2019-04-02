# coding = utf-8
#Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字,如果想体现汉字，需在全文添加
class shuxuelaoshi(object):
    def __init__(self):
        pass
    def xueshu(self):
        print ('学数学')
    def jisuan(self,num1,num2):
        return num1+num2

class yuwenlaoshi(object):
    def __init__(self,jianmianli):
        pass

    def yuwen(self,jianmianli2):
        if(jianmianli2 <=1):
            print ('学语文钱不够')
            return
        print ('学语文')
    def daren(self):
        print ('打人')

#英语老师来了，不要见面礼，有学英语的方法，需要大于两块钱，还有帮别人翻译的方法，需要英文和钱，返回汉字
class yingyulaoshi(object):
    def __init__(self):
        pass
    def xueyingyu(self,money):
        if(money <=2):
          print ('学英语钱不够')
          return
        print ('学英语')
    def fanyi(self,yingwen,money):
        return ("我是樊计玉")
    
 #w=我是一个人，做代购，钱要大于100
class songtt(object):
    def __init__(self):
        pass
    def daigou (self,money):
        if(money <=100):
            print ('钱不够，不能代购')
            return
        print ('购物成功')
        

if __name__ == '__main__':
    baba = shuxuelaoshi()
    baba.xueshu()
    a = baba.jisuan(num1=1,num2=2)
    print (a)
    
    mama = yuwenlaoshi(jianmianli=1)
    mama.yuwen(jianmianli2=2)
    mama.daren()

    wo = yingyulaoshi()
    wo.xueyingyu(money=1)
    b = wo.fanyi(yingwen='I am FJY',money=3)
    print (b)
    
    浩浩 = songtt()
    浩浩.daigou(money=120)
    
    



 

 
