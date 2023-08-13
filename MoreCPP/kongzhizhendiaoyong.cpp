//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

class Person
{
public:
    void showClassName()
    {
        cout<<"this is Person Class"<<endl;
    }
    void showPersonAge()
    {
        // if(this == NULL)
        // {
        //     return;
        // }
        // 这几行代码能够防止传入的指针式空的
        cout<<"the Person age is "<<m_age<<endl;
    }
    int m_age;
};

void test01()
{
    Person *p = NULL;
    p->showClassName();
    // p->showPersonAge();
    // 这行会导致错误的原因由于使用了m_age，而在调用属性的时候默认会使用this指针，而创建的指针是空的，无法访问成员
}

int main()
{
    test01();
    system("pause");
    return 0;
}
