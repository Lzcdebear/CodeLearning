'''
对象的属性通常会设置为 private 或者是 protected
简单的说就是不允许直接访问

对象的方法通常会是 public
因为公开的方法是对象能够接受消息，也就是对象暴露给外界的接口
这就是所谓的访问可见性

python中可以通过在对象属性前添加_来说明对象访问可见性
__name  表示一个私有属性
_name   表示一个受保护属性
'''
class Student:
    def __init__(self,name,age):
        # 创建属性
        self.__name = name
        self.__age = age
    
    # 获取私有属性
    @property
    def name(self):
        return self.__name
    
    # 修改私有属性
    @name.setter
    def name(self,name):
        self.__name = name or '无名氏'
    
    # 获取私有属性
    @property
    def age(self):
        return self.__age
    
    # 修改私有属性
    @age.setter
    def age(self,age):
        self.__age = age or '未知'
    
    
    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}')
        
# stu = Student('lzc', 17)
# stu.study('gg')
# # print(stu.__name)
# # 这里的双下划线只是py将这个属性不直接展示，不能再类外面进行调用，但是可以通过其他方法获得这个私有属性
# print(stu._Student__name)

# # 装饰器属于函数高级的应用
stu = Student('lzc',19)
print(stu.name)
stu.name = ''
print(stu.name)
