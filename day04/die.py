from random import randint

class Die():
    '''骰子类'''
    def __init__(self,num_size = 6):
        self.num_size = num_size
    
    def row(self):
        '''返回一个位于1和骰子面数之间的随机值'''
        return randint(1,self.num_size)