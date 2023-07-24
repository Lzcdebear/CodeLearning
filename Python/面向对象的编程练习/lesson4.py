class Dog:
    def __init__(self,name,age,breed,master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master
        self.sayhi()
    
    def sayhi(self):
        print('my name is %s, a %s dog, my master is %s.'%(self.name,self.breed,self.master.name))
        
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    def walk_dog(self,dog_obj):
        print('master %s take %s out for a walk' %(self.name,dog_obj.name))
        
        
