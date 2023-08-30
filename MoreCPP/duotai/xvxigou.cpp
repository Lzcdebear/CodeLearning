//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Animal
{
public:
    Animal()
    {
        cout<<"Animal构造函数调用！"<<endl;
    }

    virtual void speak()=0;

    // virtual ~Animal()
    // {
    //     cout<<"Animal虚析构函数调用！"<<endl;
    // }
    //纯虚析构函数
    virtual ~Animal()=0;
    //这里只是声明但是函数没有实际的内容，这是不被允许的，需要代码的实现
    //纯虚虚构函数也会导致animal对象变成抽象类无法实例化
};
Animal:: ~Animal()
{
    cout<<"Animal纯虚析构函数调用！"<<endl;
}


class Cat:public Animal
{
public:
    Cat()
    {
        cout<<"Cat默认构造函数调用！"<<endl;
    }

    Cat(string name)
    {
        cout<<"Cat构造函数调用！"<<endl;
        m_Name=new string(name);
    }

    virtual void speak()
    {
        cout<<*m_Name<<"Cat is speaking!"<<endl;
    }
    
    ~Cat()
    {
        if(m_Name != NULL)
        {
            cout<<"Cat析构函数调用！"<<endl;
            delete m_Name;
            m_Name=NULL;
        }
    }
    string *m_Name;
};


void test01()
{
    Animal * animal = new Cat("Tom");
    animal->speak();
    delete animal;
//在父类的指针析构的时候不会调用子类中的析构函数，导致了子类如果有堆区的属性会出现内存泄露
}

int main()
{
    test01();
    system("pause");
    return 0;
}
