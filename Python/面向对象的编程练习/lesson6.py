class Dog:
    role = 'dog'
    
    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100
        
    def bite(self,person):
        person.life_val -= self.attack_val
        print('dog[%s]bite person[%s],person hurt [%s], left life_val is [%s]'%(self.name,person.name,self.attack_val,person.life_val))
        
        
class Person:
    role = 'person'
    
    def __init__(self, name, sex, attack_val):
        self.name = name
        self.sex = sex
        self.attack_val = attack_val
        self.life_val = 100
        self.weapon = Weapon()
        
    def attack(self,dog):
        dog.life_val -= self.attack_val
        print('person[%s]attack dppg[%s],dog hurt [%s], left life_val is [%s]'%(self.name,dog.name,self.attack_val,dog.life_val))


class Weapon:
    def dog_stick(self,obj):
        self.name = 'dagoubang'
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)
        
    