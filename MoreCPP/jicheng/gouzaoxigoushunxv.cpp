//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Base
{
public:
    Base()
    {
        cout<<"Base的构造函数"<<endl;
    }

    ~Base()
    {
        cout<<"Base的析构函数"<<endl;
    }
};
class Son:public Base
{
public:
    Son()
    {
        cout<<"Son构造函数"<<endl;
    }

    ~Son()
    {
        cout<<"Son析构函数"<<endl;
    }
};

void test01()
{
    /*
        顺序为
            构造父类
            构造子类
            析构子类
            析构父类
    */
    Son s;
}



int main()
{
    test01();
    system("pause");
    return 0;
}
