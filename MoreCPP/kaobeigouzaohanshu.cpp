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



//拷贝构造函数的使用案例

// 1 使用已经创建的对象初始化新的对象
void test01()
{
    Person p1 (20);
    Person p2 (p1);
    cout<<"p1"<<endl<<p1.m_age<<endl;
    cout<<"p2"<<endl<<p2.m_age<<endl;
}
// 2 值传递的方式给函数参数传值
void doWork(Person p){}
void test02()
{
    Person p;
    doWork(p);
}
// 3 值的方式传递局部变量
Person doWork2()
{
    Person p1;
    return p1;
    // 这里return的时候就是拷贝对象返回给函数外
}
void test03()
{
    Person p = doWork2();
}

int main()
{
    // 拷贝构造函数的使用方式

    system("pause");
    return 0;
}
