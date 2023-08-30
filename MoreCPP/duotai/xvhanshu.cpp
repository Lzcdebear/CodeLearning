//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

/*
纯虚函数就是
virtual 函数名() = 0
只要类中有一个纯虚函数则会变成抽象类

抽象类无法实例对象
抽象类的子类必须重写抽象类中纯虚函数否则无法实例化对象
*/
class Base
{
public:
    virtual void func() = 0;
};

class Son:public Base
{
    virtual void func()
    {
        cout<<"Son func cout"<<endl;
    }
};

void test01()
{
    Base*base=new Son;
    base->func();
}

int main()
{
    test01();
    system("pause");
    return 0;
}
