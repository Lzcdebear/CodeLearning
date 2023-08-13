//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

//const修饰后的成员函数中无法修改成员的属性
//声明成员属性的时候加上mutable在常函数仍可以修改属性
//const修饰的对象为常对象
class Person
{
public:
    Person():m_A(10),m_B(20){}

    void showPerson() const
    {
        m_B = 100;
        //这里其实是指针指向m_B
        //而且this指针是指针常量，可以修改值，但是不能改变指针指的对象
        //所以函数后面加上const也就是
        //const Person * const this
        //使得指针常量和常量指针结合，无法改变值和指向对象
    }
    void func1()
    {
        
    }

    int m_A;
    mutable int m_B;
};

void test01()
{
    const Person p;     //在对象前加const不能修改对象的属性
    p.showPerson();     //而且常对象只能调用常函数，因为普通函数能够改变属性，所以无法调用普通函数
}

int main()
{
    test01();
    system("pause");
    return 0;
}
