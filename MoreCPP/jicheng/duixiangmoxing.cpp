//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Base
{
public:
    int m_A;
protected:
    int m_B;
private:
    int m_C;
};

class Son1:public Base
{
public:
    int m_D;
};

void test01()
{
    cout<<"size of Son1 "<<sizeof(Son1)<<endl;
}


int main()
{
    test01();
    //所有的元素都是会继承下去的
    //private 继承下去，只是无法访问，但是是保存在子类中的被隐藏了
    system("pause");
    return 0;
}

/*
可以使用开发人员命令提示符
跳转到对应盘符
跳转到路径下
dir
cl /d1 reportSingleClassLayoutSon1 (文件)
*/
