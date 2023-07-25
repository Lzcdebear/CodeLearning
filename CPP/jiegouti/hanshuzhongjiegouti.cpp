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

void PrintStudent1(student s)
{
    s.age = 100;
    cout<<s.name<<endl<<s.age<<endl<<s.score<<endl;
}

void PrintStudent2(student * p)
{
    p->score = 109823;
    cout<<p->name<<endl<<p->age<<endl<<p->score<<endl;
}


int main()
{
    student s = {"wer",12,45};
    PrintStudent1(s);
    cout<<s.age;
    PrintStudent2(&s);
    cout<<s.score;
    system("pause");
    return 0;
}
