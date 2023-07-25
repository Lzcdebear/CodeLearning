//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

struct Student
{
    string name;
    int age;
    int score;
};

int main()
{
    //创建变量
    Student s1 = {"aa",12,23};
    //指针指向变量
    Student * p = &s1;
    cout<<p<<endl;
    //指针访问数据
    cout<<p->age<<endl<<p->name<<endl<<p->score<<endl;
    system("pause");
    return 0;
}
