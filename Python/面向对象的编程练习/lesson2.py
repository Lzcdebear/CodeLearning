class Dog:
    # 这里的属性是所有实例都有的
    d_type = 'jingba' # 属性 类属性
    
    def __init__(self, name, age):
        print(f'对象名字是{name}，年龄是{age}')
        self.name = name
        self.age = age
        # self后面的name和age是self对象的属性而不是输入的变量
        
    def sayhi(self): # self 是实例本身
        print('hello, i  am a dog and my type is {}, my name is {}, i am {} years old'.format(self.d_type,self.name,self.age))
        
        
d = Dog('lzc',16) # 生成了一个实例
d2 = Dog('lzc',20)

d.sayhi()           # 虽然后面没有参数，但是默认就是self，self就是对象本身在这里也就是 d
d2.sayhi()          # 实例.方法
print(d.d_type)     # 实例.属性

# 对于实例的属性不一定只能在类里面定义，也可以通过外界定义比如
d.sex = 'male'
print(d.sex)
