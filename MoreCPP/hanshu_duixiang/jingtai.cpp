//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

//static加上关键词后为静态成员
/*
静态成员变量：
    所有对象共享同一份数据
    再搬移阶段分配内存
    类内声明，类外初始化
*/
class Person
{
public:
    static int m_A;
//静态成员变量也有访问权限
private:
    static int m_B; //类外访问不到m_B
};
int Person::m_A = 100;
int Person::m_B = 10000;
void test01()
{
    Person p1;
    cout<<p1.m_A<<endl;
    Person p2;
    p2.m_A = 200;
    cout<<p1.m_A<<endl;
}
//静态成员变量不属于某个对象，所有对象公用同一份数据
//访问方式
void test02()
{
    Person p1;
    cout<<p1.m_A<<endl;

    cout<<Person::m_A<<endl;
}


/*
静态成员函数：
    所有对象公用一个函数
    静态成员函数只能访问静态成员函数
*/
class Person1
{
public:
    static int p_A;
    int p_B;

    static void func1()
    {
        cout<<"static void func1函数调用"<<endl;
    }
private://同样，函数同样有私有共有区别
    static void func2()
    {
        p_A=600;
        // p_B = 700; //这样编写会报错
    }
};
int Person1::p_A = 900;


void test03()
{
    Person1 m1;
    m1.func1();

    Person1::func1();
}



int main()
{
    test01();
    test02();
    test03();
    system("pause");
    return 0;
}
