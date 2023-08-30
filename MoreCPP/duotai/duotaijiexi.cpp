//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;
/*
多态的实现方式原理
vfptr virtual function pointer
vftabel virutal function table 
vfpter 指针指向 vftable

animal内部结构
其中的table记录的是 &animal::speak

cat内部结构图
如果没有发生重写
    table内记录的是 &animal::speak
如果发生重写
    table内记录的是 &cat::speak
*/

class Animal
{
public:
    virtual void speak()
    //不加virutal的时候函数不属于类内的存储，大小为一个字节。而加上virtual后就会变为4个字节，这四个字节就是指针
    {
        cout<<"Speaking Now!"<<endl;
    }
};

class Cat:public Animal
{
public:
    virtual void speak()
    {
        cout<<"Cat is speaking!"<<endl;
    }
};

class Dog:public Animal
{
public:
    virtual void speak()
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




int main()
{
    test01();
    system("pause");
    return 0;
}
