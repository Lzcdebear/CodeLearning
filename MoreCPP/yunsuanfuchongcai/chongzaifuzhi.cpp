//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Person
{
public:
    Person(int age)
    {
        m_Age = new int(age);
    }

    ~Person()
    {
        if (m_Age != NULL)
        {
            delete m_Age;
            m_Age = NULL;
        }
    }


    Person& operator=(Person &p);

    int *m_Age;
};
Person& Person::operator=(Person &p)
{
    if(m_Age != NULL)
    {
        delete m_Age;
        m_Age = NULL;
    }
    m_Age = new int(*p.m_Age);
    return *this;
}


void test01()
{
    Person p1(18);
    Person p2(20);
    cout<<"p1 age is "<<*p1.m_Age<<endl;
    cout<<"p2 age is "<<*p2.m_Age<<endl;
    p1 = p2;
    cout<<"p1 = p2 later p2 is "<<*p2.m_Age<<endl;
    Person p3(30);
    p1=p2=p3;
    cout<<*p1.m_Age<<endl<<*p2.m_Age<<endl<<*p3.m_Age<<endl;
    cout<<"test01 finished"<<endl;
}

int main()
{
    test01();
    int a =10;
    int b = 20;
    int c = 30;
    c = b = a;
    cout<<a<<endl<<b<<endl<<c<<endl;
    system("pause");
    return 0;
}
