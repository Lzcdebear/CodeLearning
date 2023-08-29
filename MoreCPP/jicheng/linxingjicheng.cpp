//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

//利用虚继承方法解决重复m_Age问题
//animal 为虚基类
class Animal
{
    public:
    int m_Age;
};

class Sheep:virtual public Animal
{};

class Tuo:virtual public Animal
{};

class YnagTuo:public Sheep,public Tuo
{};

/*
会产生一个指针，指向虚基类表格
vbptr 指向 vbtable
animal会产生唯一的m_Age
而其余的sheep和tuo只会继承指针和偏移
通过偏移可以使指针指向animal的m_Age
这样只会有一份数据
*/

void test01()
{
    YnagTuo yt;
    yt.Sheep::m_Age = 18;
    yt.Tuo::m_Age = 28;
}

int main()
{
    test01();
    system("pause");
    return 0;
}
