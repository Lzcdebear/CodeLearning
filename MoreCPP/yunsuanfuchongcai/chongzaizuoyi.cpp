//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Person
{
    friend ostream& operator<<(ostream&cout,Person &p);
public:
    Person(int a,int b)
    {
        m_A = a;
        m_B = b;
    }
private:
    // void operator<<()
    // 无法使用成员函数定义<<运算符重载
    int m_A;
    int m_B;
};

ostream& operator<<(ostream&cout,Person &p)
{
    cout << "m_A " << p.m_A << "  m_B " << p.m_B;
    return cout;
}


void test01()
{
    Person p (10,80);
    cout<<p;
    cout<<endl;
}

int main()
{
    test01();
    system("pause");
    return 0;
}
