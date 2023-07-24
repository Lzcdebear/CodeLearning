class Dog:
    d_type = 'jingba' # 属性 类属性
    
    
    def sayhi(self): # self 是实例本身
        print('hello, i  am a dog and my type is', self.d_type)
        
        
d = Dog() # 生成了一个实例
d2 = Dog()

d.sayhi()
d2.sayhi()          # 实例.方法
print(d.d_type)     # 实例.属性