class Student:
    # 初始化方法 给当前对象创建属性
    def __init__(self, name, age):
        # 给当前类添加属性
        self.name = name
        self.age = age
        
    def study(self, course_name):
        # 属性使用self进行调用，参数直接调用
        print(f'{self.name}正在学习{course_name}')
        
    def play(self):
        print(f'{self.name}正在玩游戏')
        
    # 使用内置的魔术方法进行实现打印自己创建的内容
    def __repr__(self):
        return f'{self.name}:{self.age}'
        
# 实例化类
stu1 = Student('lzc',19)
# 打印当前对象
print(stu1)

stu1.study('Python')

stu2 = Student('lyf',19)
stu2.play()
