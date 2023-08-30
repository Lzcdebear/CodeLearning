//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

class Person
{
    // 1 构造函数没有返回值，不用写void
    // 2 函数名和类名相同
    // 3 可以有参数可以重载
    // 4 会自动调用，只会调用一次
public:
    Person()
    {
        cout<<"默认构造/无参构造函数"<<endl;
    }

    Person(int a)
    {
        cout<<"有参构造函数"<<endl;
    }

    Person(const Person &a) //使用引用的方式传递
    {
        cout<<"拷贝构造函数"<<endl;
        age = a.age;
    }

    // 1 构造函数没有返回值，不用写void
    // 2 函数名和类名相同,前面加 ~
    // 3 不可以有参数
    // 4 会自动调用，只会调用一次
    ~Person()
    {
        cout<<"析构函数"<<endl;
    }

    int age;
};


// 构造函数初始化


void test01()
{
    // 括号法
    // Person a; //在栈区的数据，在调用完了之后会自动销毁。
    // Person b(10);
    // Person c(b);
    // // 使用默认构造的时候不要添加小括号
    // // 因为编译器会认为这是函数的声明
    // cout<<"b age is "<<b.age<<endl;
    // cout<<"c age is "<<c.age<<endl;

    // 显示法
    // Person a; //在栈区的数据，在调用完了之后会自动销毁。
    // Person b = Person(10);
    // // 这里等号右侧的Person(10)单独拿出来是一个匿名对象，是一个创建出来的对象但是没有名字
    // // 匿名对象会在当前行执行完了之后立刻释放
    // // 上面显示法就是创造出来一个匿名对象，然后命名为 b，变成有名字的对象
    // // 不要利用拷贝对象函数初始化匿名对象 编译器会认为
    // // Person(c) === Person c 是对象的声明，但是对象c已经定义完了
    // Person c = Person(b);
    // cout<<"b age is "<<b.age<<endl;
    // cout<<"c age is "<<c.age<<endl;

    // 隐式转化法
    Person a = 10; // Person a = 10  === Person a = Person 10
    Person b = a;
}

int main()
{
    // 对象的初始化设置
    // 初始化函数使用   构造函数
    // 清理函数使用     析构函数
    // 两个函数使用系统自动调用，是系统会自动调用的，系统自动就是使用 空 的，可以自定义
    test01();

    Person b;   // 在main中会一直挂起，直到return 0之后析构
    system("pause");
    return 0;
}
