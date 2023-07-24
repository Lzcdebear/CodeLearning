'''
类      把行为相同的对象为类
对象    一组数据和处理数据的方法组成对象
'''

# 在python中可以使用 class 加上类名进行定义类
class Students:
    # 如果函数在类中，则被称之为类方法
    def study(self,course_name):
        print(f'学生正在学习{course_name}')
    
    def play(self):
        print(f'学生正在游戏')
'''
定义了一个学生类
    定义了方法
    
    每一位学生的行为都是不一样的，这个行为就是方法
'''

# 当前的 stu1 是 Student 这个类的对象，是一个具体的实例
stu1 = Students()
stu2 = Students()
# # 当前输出的值为具体实例在内存中的地址 十六进制的值
# print(stu1)
# print(stu2)
# # 当前输出的值为具体实例在内存中的地址 十进制的值
# print(id(stu1))
# print(id(stu2))
# # 可以使用 hex 进行十进制转化为十六进制
# print(hex(id(stu1)),hex(id(stu2)))

# 通过对象.方法进行类方法的调用
stu1.study('Python Courses')
# 需要对当前的类进行实例化，也就是加上()
Students().study('Java Courses')

