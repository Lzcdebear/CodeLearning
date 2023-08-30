//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

//这是一种语法来初始化对象
class Person
{
public:
    // Person(int a,int b,int c)
    // {
    //     m_A = a;
    //     m_B = b;
    //     m_C = c;
    // }//传统方式

    //初始化列表的方法
    Person():m_A(10),m_B(20),m_C(30){}
    Person(int a,int b,int c):m_A(a),m_B(b),m_C(c){}
    //在{}中仍可以继续进行操作，而对象的值已经初始化
    int m_A;
    int m_B;
    int m_C;
};

int main()
{
    system("pause");
    return 0;
}
