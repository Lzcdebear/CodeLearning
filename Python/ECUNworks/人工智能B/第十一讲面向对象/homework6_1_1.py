'''
请创建一个Circle（圆）类，该类有一个属性：半径r；有一个构造方法，可接收外界传入的参数设置到属性r中；另外定义了４个方法，方法area用于计算面积，方法girth用于计算周长，方法setR用于设置半径r，方法getR用于读取半径r。
（π常量可用math.pi。用于测设Circle类的主程序已给出。）
'''

import math
class Circle:
    def __init__(self,r):
        self.r = float(r)
        
    def area(self):
        return self.r * self.r * math.pi
        
    def girth(self):
        return self.r * 2 * math.pi
        
    def setR(self,R):
        self.r = float(R)
    
    def getR(self):
        return self.r
        

#主程序
r = 5.0;
cc = Circle(r);
print("半径为%.2f的圆的周长是：%.2f，面积是：%.2f\n"%(r,cc.girth(),cc.area()));
cc.setR(8.0);
print("半径为%.2f的圆的周长是：%.2f，面积是：%.2f\n"%(cc.getR(),cc.girth(),cc.area()));



'''
请定义Employee类和其子类Manager类。
Employee类包含三个属性：
雇员姓名（name），年龄（age），业绩评等（grade），
业绩评等从高到低为A,B,C,D四等。Manager类继承Employee类，
并定义了两个新属性：department代表该 Manager所管辖部门（字符串类型），
subm代表该Manager管理的所有Employee（列表类型）。主程序已给出。
'''
class Employee:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        
class Manager(Employee):
    def __init__(self, name, age, grade, department, subm):
        super().__init__(name, age, grade)
        self.department = department
        self.subm = subm
        
        
person1 = Employee("张三",35,'A')
person2 = Employee("李四",28,'B')
manager1 = Manager("王五",42,'A',"财务部",[person1,person2])
print("经理姓名为%s，年龄为%d，业绩评等为%s，所管理部门为%s"%(manager1.name,manager1.age,manager1.grade,manager1.department))
print("下属雇员有：",end=" ")
for i in range(len(manager1.subm)):
    print(manager1.subm[i].name,end=",")