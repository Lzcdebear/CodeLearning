//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    //定义指针
    int a = 10;
    //定义方法 数据类型 * 指针名称
    int * p;
    p = &a;
    cout<<"address"<<&a<<endl;
    cout<<p<<endl;
    *p = 1000; //解引用的操作，找到指针指向的内存中的数据
    cout<<a<<endl;
    cout<<*p<<endl;
    cout<<p<<endl;
    system("pause");
    return 0;
}

