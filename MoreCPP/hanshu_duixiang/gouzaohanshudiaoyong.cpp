//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;


class Person
{
public:
    Person()
    {
        cout<<"Person默认构造函数调用"<<endl;
    }

    ~Person()
    {
        cout<<"Person析构函数调用"<<endl;
    }

    Person(int age)
    {
        m_age = age;
        cout<<"Person含参构造函数调用"<<endl;
    }

    Person(const Person & p)
    {
        m_age = p.m_age;
        cout<<"Person拷贝构造函数调用"<<endl;
    }

    int m_age;
};


int main()
{
    
    system("pause");
    return 0;
}