# coding=utf-8
class shuxuelaoshi(object):
    def __init__(self):
        pass
    def xueshu(self):
        print '学数学'
    def jisuan(self,num1,num2):
        return num1+num2

class yuwenlaoshi(object):
    def __init__(self,jianmianli):
        pass

    def yuwen(self,jianmianli2):
        if(jianmianli2 <=1):
            print '学语文钱不够'
            return
        print '学语文'
    def daren(self):
        print '打人'

class yingyulaoshi(object):
    def __init__(self):
        pass
    def xueyingyu(self,money):
        if(money <=2):
          print '学英语钱不够'
          return
        print '学英语'
    def fanyi(self,yingwen,money):
        return "我是樊计玉"

if __name__ == '__main__':
    baba = shuxuelaoshi()
    baba.xueshu()
    a = baba.jisuan(num1=1,num2=2)
    print a

    mama = yuwenlaoshi(jianmianli=1)
    mama.yuwen(jianmianli2=2)
    mama.daren()

    wo = yingyulaoshi()
    wo.xueyingyu(money=1)
    b = wo.fanyi(yingwen='I am FJY',money=3)
    print b

    #英语老师来了，不要见面礼，有学英语的方法，需要大于两块钱，还有帮别人翻译的方法，需要英文和钱，返回汉字

