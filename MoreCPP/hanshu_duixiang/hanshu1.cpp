//对于函数可以在创建函数的时候就进行默认值的设定，规定是从左向右第一个设置默认值的量后面所有都必须要有默认值
//默认值在传入的时候如果没有传入具体的数值就会使用默认值，但是如果传入了数值则会使用传入的数值
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

//对于函数声明的时候已经有默认参数的函数在定义的时候不能再次定义默认参数
int func2(int a=10, int b=20);

void func1(int a,int b=2, int c=30)
{
    int d = a+b+c;
    cout<<d<<endl;
}

int func2(int a, int b)
{
    return a+b;
}

int main()
{
    func1(10);
    func1(10,90);
    func1(10,90,100);

    system("pause");
    return 0;
}
