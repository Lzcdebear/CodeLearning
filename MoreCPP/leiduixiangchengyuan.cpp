//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

class Phone
{
public:
    Phone(string brand):brand(brand)
    {
        cout<<"Phone构造函数调用"<<endl;
    }

    ~Phone()
    {
        cout<<"Phone析构函数调用"<<endl;
    }

    string brand;
};

class Person
{
public:
    Person(string name,string brand):name(name),phone(brand)
    {
        cout<<"Person构造函数调用"<<endl;
    }

    ~Person()
    {
        cout<<"Person析构函数调用"<<endl;
    }

    string name;
    Phone phone;

};

void test01()
{
    //当其他类的对象作为对象的成员的时候先构造其他对象再构造自身对象
    Person p("张三","iPhone Pro");
    cout<<"Phone name  "<<p.phone.brand<<"    name  "<<p.name<<endl;
    //在析构的时候先析构自身再析构其他函数对象
}

int main()
{
    test01();
    system("pause");
    return 0;
}
