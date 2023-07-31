//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

//这里将要创建类
//类中有属性和方法，也就是两者都成为成员
//类中的属性一般是量，方法一般是函数
class Person        
//和struct是一样的道理，struct也是类，但是两者的访问权限不同
//在class中定义的属性和类默认都是私有的
//在struct中定义的属性和类默认都是公共

/*
对于class默认对象为私有的访问权限
可以使用定义额外的函数来进行属性的访问，因为函数是类内部的，也可以使用函数来进行属性的更改
而利用函数来访问或者更改属性的好处就是能够对输入或者输出进行限制或者更改
比如访问age
if (age < 0||age > 1000)
{
    return;
}
else:
{
    m_age = age;
}
*/
{
    //这里展示的就是类的属性，可以包括不同的访问权限
    /*
    public      公共权限    类内可以访问，类外也可以访问
    protected   保护权限    类内可以访问，类外不可以访问
    private     私有权限    类内可以访问，类外不可以访问
    */
    public:
        string m_name;
    
    protected:
        string m_car;
    
    private:
        int m_password;
    
};

int main()
{
    
    system("pause");
    return 0;
}
