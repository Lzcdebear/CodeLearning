//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class MyInteger
{
    friend ostream& operator<<(ostream&cout,MyInteger p);
public:
    //构造函数初始化为0
    MyInteger()
    {
        m_Num = 0;
    }
    //重载前置
    MyInteger& operator++();
    //重载后置
    MyInteger operator++(int);
private:
    int m_Num;
};

//重载<<输出MyInteger
ostream& operator<<(ostream&cout,MyInteger p)
{
    cout << p.m_Num;
    return cout;
}
//test01输出MyInteger
void test01()
{
    MyInteger myint;
    cout<<myint<<endl;
}
//前置递增
MyInteger & MyInteger::operator++()
{
    m_Num++;
    return *this;
}
//后置递增
MyInteger MyInteger::operator++(int)
{
    MyInteger temp = *this;
    m_Num++;
    return temp;
}
//test02前置递增，先增加值再返回，输入0，返回1，实际值1
void test02()
{
    MyInteger myint;
    cout<<"test02"<<endl;
    cout<<++(++myint)<<endl;
}
//test03后置递增，先返回再增加值，输入0，返回0，实际值1
void test03()
{
    MyInteger myint;
    cout<<"test03"<<endl;
    cout<<(myint++)<<endl;
    cout<<"myint is ";
    cout<<myint;
}


int main()
{
    test01();
    test02();
    test03();
    system("pause");
    return 0;
}
