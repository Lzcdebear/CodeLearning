//无论心情怎么样，今天也要继续加油学习哦
#include <iostream>
#include <cmath>
#include <string>

using namespace std;

struct student
{
    string name;
    int age;
    int score;
};

struct teacher
{
    int id;
    string name;
    int age;
    student stu;
};

int main()
{

    teacher t;
    t.id=1000;
    t.name = "aaa";
    t.age = 50; 

    t.stu.name = "wewe";
    t.stu.age = 12;
    t.stu.score = 78;

    cout<<t.name<<endl<<t.id<<endl<<t.age<<endl<<t.stu.age<<endl<<t.stu.name<<endl<<t.stu.score<<endl;
    system("pause");
    return 0;
}
