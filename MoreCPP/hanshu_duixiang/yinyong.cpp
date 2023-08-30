//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void mySwap01(int a, int b)//值传递，传入的a和b不改变
{
    int temp =a;
    a = b;
    b = temp;
}

void mySwap02(int* a, int* b)//地址传递，传入的a和b改变
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void mySwap03(int &a, int &b)//引用传递，传入的a和b改变
{
    int temp = a;
    a = b;
    b = temp;
}


int main()
{
    int a = 10;
    int &b = a;
    cout<<b<<endl;
    cout<<a<<endl;
    cout<<&b<<endl;
    cout<<&a<<endl;
    //a 和 b 的内存地址是一样的
    b = 20;
    int c = 90;
    b = c;
    cout<<a<<endl<<b<<endl;
    cout<<&a<<endl<<&b<<endl<<&c<<endl;
    //引用一旦创建了就不能改变引用的对象，例如上面的 b=c 表达的是赋值运算而不是引用
    cout<<a<<"  "<<b<<endl;

    a = 10;
    b = 20;
    mySwap01(a,b);
    cout<<a<<b<<endl;
    a = 10;
    b = 20;
    mySwap02(&a,&b);
    cout<<a<<b<<endl;
    a = 10;
    b = 20;
    mySwap03(a,b);
    cout<<a<<b<<endl;
    system("pause");
    return 0;
}
