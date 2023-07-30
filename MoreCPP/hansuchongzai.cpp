//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;
//函数重载      函数名相同的不同函数，加强函数的复用性
//条件  必须在同一个作用域下
//      函数名称相同
//      函数的参数类型不同，个数不同，顺序不同
void func()
{
    cout<<"func的调用 The First"<<endl;
}

void func(int a)
{
    cout<<"func的调用 The Second"<<endl;
}

int main()
{
    func();
    func(1);
    system("pause");
    return 0;
}
