//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Person
{
public:
    Person(string name,int age)
    {
        m_Name = name;
        m_Age = age;
    }

    bool operator==(Person &p);
    bool operator!=(Person &p);
    string m_Name;
    int m_Age;
};
bool Person::operator==(Person &p)
{
    if(this->m_Name == p.m_Name && this->m_Age==p.m_Age)
    {
        return true;
    }
    else
    {
        return false;
    }
}
bool Person::operator!=(Person &p)
{
    if(this->m_Name == p.m_Name && this->m_Age==p.m_Age)
    {
        return false;
    }
    else
    {
        return true;
    }
}

void test01()
{
    Person p1("Tom",18);
    Person p2("Tom",28);
    if(p1==p2)
    {
        cout<<"p1 == p2"<<endl;
    }
    if(p1!=p2)
    {
        cout<<"p1 != p2"<<endl;
    }
}

int main()
{
    test01();
    system("pause");
    return 0;
}
