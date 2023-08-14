//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

/*
调用的重载也就是小括号的重载()
在重载后的使用方式和函数非常像，所以也被称为
    仿函数
*/
class MyPrint
{
public:
    void operator()(string test)
    {
        cout<<test<<endl;
    }
};

class MyAdd
{
public:
    int operator()(int num1,int num2)
    {
        return num1+num2;
    }
};

void test01()
{
    MyPrint myprint;
    myprint("Hello World");
}
void test02()
{
    MyAdd myadd;
    int ret = myadd(100,100);
    cout<<ret<<endl;
}
int main()
{
    test01();
    system("pause");
    return 0;
}
