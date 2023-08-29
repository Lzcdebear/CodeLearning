//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

class Java
{
public:
    void header()
    {
        cout<<"首页、公开课、登录、注册"<<endl;
    }

    void footer()
    {
        cout<<"帮助中心、交流合、站内地图"<<endl;
    }

    void left()
    {
        cout<<"Java、Python、C++"<<endl;
    }

    void content()
    {
        cout<<"Java视频内容..."<<endl;
    }
};

//使用继承的技术
class BasePage
{
public:
    void header()
    {
        cout<<"首页、公开课、登录、注册"<<endl;
    }

    void footer()
    {
        cout<<"帮助中心、交流合、站内地图"<<endl;
    }

    void left()
    {
        cout<<"Java、Python、C++"<<endl;
    }
};
//使用继承创建python页面
class Python:public BasePage
{
public:
    void content()
    {
        cout<<"Python视频内容..."<<endl;
    }
};
class Cpp:public BasePage
{
public:
    void content()
    {
        cout<<"Cpp视频内容..."<<endl;
    }
};

void test01()
{
    Java ja;
    cout<<"Java的页面内容如下："<<endl;
    ja.header();
    ja.footer();
    ja.left();
    ja.content();
    cout<<"---------------------------------------"<<endl;
}
//继承测试
void test02()
{
    Python py;
    cout<<"Python的页面内容如下："<<endl;
    py.header();
    py.footer();
    py.left();
    py.content();
    cout<<"---------------------------------------"<<endl;
    Cpp cp;
    cout<<"Cpp的页面内容如下："<<endl;
    cp.header();
    cp.footer();
    cp.left();
    cp.content();
    cout<<"---------------------------------------"<<endl;
}

int main()
{
    test01();
    test02();
    system("pause");
    return 0;
}
