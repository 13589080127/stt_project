class songtt(object):
    def __init__(self):
        pass
    def daigou (self,money):
        if(money <=100):
            print ('钱不够，不能代购')
            return
        else:#如果if中有return时，else可不用写
            print('购物成功')
            
            


if __name__ == '__main__':
    浩浩 = songtt()
    浩浩.daigou(money=120)
    
    

    
    
    
    
        