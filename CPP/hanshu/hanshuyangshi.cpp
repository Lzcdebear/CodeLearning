//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

// 无参数无返回值
void test01()
{
    cout<<"this is test01"<<endl;
};
// 有参数无返回值
void test02(int a)
{
    cout<<"this is test02 a = "<<a<<endl;
};
// 无参数有返回值
int test03()
{
    cout<<"this is test03"<<endl;
    return 1000;
};
// 有参数有返回值
int test04(int a)
{
    cout<<"this is test04 a ="<<a<<endl;
    return a;
};


int main()
{
    test01();

    test02(100);

    int num1 = test03();
    cout<<num1;

    int num2 = test04(100000);
    cout<<num2;

    system("pause");
    return 0;
}

