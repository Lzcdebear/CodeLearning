//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Base
{
public:
    Base()
    {
        m_A=100;
    }

    void func()
    {
        cout<<"func from Base cout"<<endl;
    }

    void func(int a)
    {
        cout<<"func int "<<a<<" from Base cout"<<endl;
    }

    int m_A;
};
class Son:public Base
{
public:
    Son()
    {
        m_A=200;
    }

    void func()
    {
        cout<<"func from Son cout"<<endl;
    }

    int m_A;
};

void test01()
{
    Son s;
    cout<<"m_A from Son"<<endl<<s.m_A<<endl;
    cout<<"m_A from Base"<<endl<<s.Base::m_A<<endl;
}

void test02()
{
    Son s;
    s.func();
    s.Base::func();
    s.Base::func(100);
    //子类中如果又同名的函数，则会隐藏所有父类中的同名函数包括函数重载
}


int main()
{
    test01();
    test02();
    system("pause");
    return 0;
}
