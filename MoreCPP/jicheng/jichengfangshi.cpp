//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

/*
这里介绍的是继承的方式不同的话产生的子类属性也是不同的
比如
class A(也就是父类)
{
    public int a
    protected int b
    private int c
}
这里private代表的意思是私有的，也就是无法继承的
三种继承方式    public/protected/private

public 继承 A
class B public A
{
    public int a
    protect int b
}

protected 继承 A
class B protected A
{
    protect int a, int b
}

private 继承 A
class B private A
{
    private int a, int b
}
*/
void printword()
{
    cout<<"这里介绍的是继承的方式不同的话产生的子类属性也是不同的\n比如\nclass A(也就是父类)\n{\n\tpublic int a\n\tprotected int b\n\tprivate int c\n}\n这里private代表的意思是私有的，\
    也就是无法继承的\n三种继承方式    public/protected/private\n\npublic 继承 A\nclass B public A\n{\n\tpublic int a\n\tprotect int b\n}\n\nprotected 继承 A\nclass B \
    protected A\n{\n\tprotect int a, int b\n}\n\nprivate 继承 A\nclass B private A\n{\n\tprivate int a, int b\n}"<<endl;
}

int main()
{
    printword();
    system("pause");
    return 0;
}
