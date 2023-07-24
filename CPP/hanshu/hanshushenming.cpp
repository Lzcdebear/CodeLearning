//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

// 使用函数的声明能够将函数存在使得在main中运行不出现问题
int max (int a, int b);

int main()
{
    int a = 10;
    int b = 20;
    int c = max(a,b);
    cout<<c<<endl;
    system("pause");
    return 0;
}

// 如果自己定义的代码在函数后面则会出现报错，因为代码是依次运行的
// 而如果代码在main前面则不会出现问题
// 而声明能够有多次，但是定义只能有一次
int max (int a, int b)
{
    return a>b ? a : b;
}