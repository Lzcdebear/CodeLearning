//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class AbstractDrinking
{
public:
    virtual void Boil() = 0;
    virtual void Brew() = 0;
    virtual void PourInCup() = 0;
    virtual void Addtaste() = 0;
    void MakeDrink()
    {
        Boil();
        Brew();
        PourInCup();
        Addtaste();
    }
};

class MakeTea:public AbstractDrinking
{
public:
    virtual void Boil()
    {
        cout<<"Start Boiling Water..."<<endl;
    }

    virtual void Brew()
    {
        cout<<"Start Brewing Tea..."<<endl;
    }

    virtual void PourInCup()
    {
        cout<<"Start Pouring Tea In Cup..."<<endl;
    }

    virtual void Addtaste()
    {
        cout<<"Start Adding Flowers To Tea..."<<endl;
    }
};

class MakeCoffee:public AbstractDrinking
{
public:
    virtual void Boil()
    {
        cout<<"Start Boiling Milk..."<<endl;
    }

    virtual void Brew()
    {
        cout<<"Start Brewing Coffee..."<<endl;
    }

    virtual void PourInCup()
    {
        cout<<"Start Pouring Coffee In Cup..."<<endl;
    }

    virtual void Addtaste()
    {
        cout<<"Start Adding Milk To Coffee..."<<endl;
    }
};

void DoWork(AbstractDrinking * abs)
{
    abs->MakeDrink();
    cout<<"---------------------------------"<<endl;
    delete abs;
}

void test01()
{
    DoWork(new MakeCoffee);
    DoWork(new MakeTea);
}

int main()
{
    test01();
    system("pause");
    return 0;
}
