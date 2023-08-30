//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;
//this指针作用
//解决名称冲突
//返回对象本身
//实际上this就是一个指针指向对象本身，也就是使用class这种类的哪个对象就指向那个
//比如 p1.addage(10) 在调用这个函数的时候 this 指针就会指向 p1
class Person
{
public:
    Person(){}

    Person(int age)
    {
        this->age=age;//这里编译器理解的是三个age是同一个，也就是age其实是随机的
    }

    Person PersonaAddAge(Person &p)
    {
        this->age += p.age;
        return *this;   //这时候会调用拷贝构造函数，创建一个新的对象
    }

    int age;
    // //非静态成员变量，如果是空的对象，占用一个字节
    // int m_A;
    // //静态成员变量，不占用对象内存空间
    // static int m_B;
    // //非静态成员函数
    // void func1(){}
    // //静态成员函数
    // static void func2(){}
};

void test01()
{
    Person p;
    cout<<"size of p = "<<sizeof(p)<<endl;
}
void test02()
{
    Person p1(18);
    cout<<"p1 age is "<<p1.age<<endl;
}
void test03()
{
    Person p1(18);
    Person p2(19);

    p2.PersonaAddAge(p1).PersonaAddAge(p1);
    cout<<"p2 age is "<<p2.age<<endl;
}


int main()
{
    test01();
    test02();
    test03();
    system("pause");
    return 0;
}
