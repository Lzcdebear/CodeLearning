class RealtionShip:
    def __init__(self):
        self.couple = []
        
    def make_couple(self,obj1,obj2):
        self.couple = [obj1,obj2]
        print('%s and %s are couple now'%(obj1,obj2))
        
    def get_my_parter(self,obj):
        print('find %s parter'%(obj.name))
        for i in self.couple:
            if i != p1:
                return i
            else:
                print('You dont have any couple, my poor boy')
                
    def break_up(self):
        print('%s and %s break up from now on'%(self.couple[0].name,self.couple[1].name))
        self.couple.clear()


class Person:
    def __init__(self,name,age,sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation
        self.parter = None # 使用这中方式进行关联机会导致关联是单向的，需要双方都设置
        
    def do_private_stuff(self):
        pass
    
relation_obj = RealtionShip()
p1 = Person('majiji',24, 'M',relation_obj)
p2 = Person('liyaya',22,'F',relation_obj)

relation_obj.make_couple(p1,p2)

p1.parter = p2
p2.parter = p1

print(p1.parter.name)
print(p2.parter.name)

print(p1.relation.get_my_parter(p1).name)

print(p1.relation.break_up())