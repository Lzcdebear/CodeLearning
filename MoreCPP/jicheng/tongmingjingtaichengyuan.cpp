//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

//静态成员所有对象共有一个内容
//静态成员函数只能访问静态成员对象
class Base
{
public:
    static void func()
    {
        cout<<"Static func from Base cout"<<endl;
    }

    static void func(int a)
    {
        cout<<"Static func int a from Base cout "<<a<<endl;
    }
    static int m_A;
};
int Base::m_A =100;


class Son:public Base
{
public:
    static void func()
    {
        cout<<"Static func from Son cout"<<endl;
    }

    static int m_A;
};
int Son::m_A = 200;

void test01()
{
    Son s;
    cout<<"m_A from son "<<endl<<s.m_A<<endl;
    cout<<"m_A from base"<<endl<<s.Base::m_A<<endl;
    cout<<"m_A from son without Son s"<<endl<<Son::m_A<<endl;
    cout<<"m_A from base without Son s"<<endl<<Son::Base::m_A<<endl;
}

void test02()
{
    Son s;
    s.func();
    s.Base::func();
    Son::func();
    Son::Base::func();
    s.Base::func(100);
}

int main()
{
    test01();
    test02();
    system("pause");
    return 0;
}
