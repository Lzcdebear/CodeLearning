//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

/*
静态多态    重载    函数地址早绑定
动态多态            函数地址需要的时候才绑定
*/
class Animal
{
public:
    virtual void speak()
    {
        cout<<"Speaking Now!"<<endl;
    }
};

class Cat:public Animal
{
public:
    void speak()
    {
        cout<<"Cat is speaking!"<<endl;
    }
};

class Dog:public Animal
{
public:
    void speak()
    {
        cout<<"Dog is speaking!"<<endl;
    }
};

//这里提前绑定了地址，是animal，如果想让运行的时候绑定，也就是让cat说话就需要晚绑定
void doSpeak(Animal &animal)
{
    animal.speak();
}

void test01()
{
    Cat cat;
    doSpeak(cat);

    Dog dog;
    doSpeak(dog);
}

//动态多态
//需要继承关系
//子类需要重写父类的virtual函数

//使用的方式则为父类的引用或者指针指向子类


int main()
{
    test01();
    system("pause");
    return 0;
}