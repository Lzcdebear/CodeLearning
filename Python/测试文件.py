class TellWhat():
    def __init__(self):
        self.name = ''
    
    def TellTheFood(self,name):
        self.name = '鸭脖'
        print('这个食物是',self.name)

food = input('这个食物是什么')
tellwhat = TellWhat()
tellwhat.TellTheFood(food)