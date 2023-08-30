//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

/*
全局函数做友元
类也可以
成员函数也可以
*/
class GoodBoy;
class GoodGay;

class Building
{
    friend void goodGay(Building &build);
    friend class GoodGay;
public:
    Building()
    {
        m_Bedroom = "卧室";
        m_Sittingroom = "客厅";
    }
public:
    string m_Sittingroom;

private:
    string m_Bedroom;
};
//全局函数
void goodGay(Building &build)
{
    cout<<"正在访问Building中的"<<build.m_Sittingroom<<endl;
    cout<<"正在访问Building中的"<<build.m_Bedroom<<endl;
}

//类
class GoodGay
{
public:
    GoodGay()
    {
        building = new Building;
    }
    void visit();
    Building *building;
};
void GoodGay::visit()
{
    cout<<"GoodGay正在访问"<<building->m_Sittingroom<<endl;
    cout<<"GoodGay正在访问"<<building->m_Bedroom<<endl;
}

class GoodBoy
{
public:
    GoodBoy();
    void visit();
    void privisit();
    Building *building;
};
GoodBoy::GoodBoy()
{
    building = new Building;
}
void GoodBoy::visit()
{
    cout<<"正在访问"<<building->m_Sittingroom<<endl;
}
void GoodBoy::privisit()
{
    cout<<"正在访问"<<endl;
}

void test01()
{
    Building build;
    goodGay(build);
}
void test02()
{
    GoodGay gg;
    gg.visit();
}
void test03()
{
    GoodBoy gg;
    gg.visit();
    gg.privisit();
}

int main()
{
    test01();
    test02();
    test03();
    system("pause");
    return 0;
}
