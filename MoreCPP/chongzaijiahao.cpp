//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Person
{
public:
    int m_A;
    int m_B;

    Person operator+(Person &p)
    {
        Person temp;
        temp.m_A = this->m_A + p.m_A;
        temp.m_B = this->m_B + p.m_B;
        return temp;
    }
};
// 在全局函数中也可以使用定义这样的函数进行定义操作
// Person operator+(Person &p1, Person &p2)
// {
//     Person temp;
//     temp.m_A = p1.m_A + p2.m_A;
//     temp.m_B = p1.m_B + p2.m_B;
//     return temp;
// }


void test01()
{
    Person p1;
    p1.m_A=10;
    p1.m_B=20;
    Person p2;
    p2.m_A=30;
    p2.m_B=40;

    Person p3 = p1+p2;
    /*
        对于成员函数而言，上面这行代码等价于
            p3 = p1.operator+(p2);
        对于全局函数而言，上面这行代码等价于
            p3 = operator+(p1,p2);
        直接使用 + 是一种简化的方式
    */
    cout<<p3.m_A<<endl;
    cout<<p3.m_B<<endl;
}

int main()
{
    test01();
    system("pause");
    return 0;
}
